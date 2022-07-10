#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  wiki.py
#
#  Copyright 2022 Thomas Castleman <contact@draugeros.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
"""Wiki markdown parser and interpolater"""
import time
import os
import markdown
from flask import render_template
import common


def list_posts():
    """List all available posts"""
    posts = os.listdir("post-meta/wiki")
    meta = {}
    for each in posts:
        meta[each] = get_post_metadata(each)
        meta[each] = time.strptime(meta[each]["WRITTEN"],
                                   common.settings["time-format-displayed"])
        meta[each] = time.mktime(meta[each])
    del posts
    output = []
    keys = list(meta.keys())
    for each in range(len(keys)):
        most = [0, ""]
        for each1 in keys:
            if meta[each1] > most[0]:
                most[0] = meta[each1]
                most[1] = each1
        output.append(most[1])
        del keys[keys.index(most[1])]
    return output



def get_post_metadata(title):
    """Get a post's metadata"""
    path = f"post-meta/wiki/{title}"
    if os.path.exists(path):
        with open(path, "r") as file:
            metadata_raw = file.read().split("\n")
    else:
        raise FileNotFoundError(f"{path} not found")

    # parse out comments  and blank lines from metadata
    for each in range(len(metadata_raw) - 1, -1, -1):
        if metadata_raw[each] == "":
            del metadata_raw[each]
        elif metadata_raw[each][0] == "#":
            del metadata_raw[each]

    # parse into dictionary
    metadata = {}
    for each in enumerate(metadata_raw):
        data = each[1].split(": ")
        if data[0].lower() in ("tags", "author", "editor"):
            metadata[data[0].upper()] = data[1].split(",")
        elif data[0].lower() == "written":
            metadata[data[0].upper()] = time.strptime(data[1],
                                              common.settings["time-format-stored"])
        elif data[0].lower() == "synopsis":
            # limit synopsis length to 140 characters
            metadata[data[0].upper()] = data[1][:common.settings["synopsis-length"]]
    keys = ["SYNOPSIS" , "TAGS", "AUTHOR", "WRITTEN"]
    metadata["WRITTEN"] = time.strftime(common.settings["time-format-displayed"],
                                        metadata["WRITTEN"])
    if not all(item in metadata.keys() for item in keys):
        raise TypeError(f"Not all fields of { keys } in { path }")
    return metadata


def search_tags(tags: (list, tuple), method=True):
    """Search for entries which match a given tag or tags

    method can be one of 3 values: True, False, or None

    if method == True, entry must have ALL tags. This is the default behavior.
    if method == False, entry must have NONE of tags.
    if method == None, entry may have one or more of tags.
    """
    if not isinstance(tags, (list, tuple)):
        raise TypeError(f"{tags} is not of type list or tuple")
    posts = list_posts()
    post_meta = {}
    for each in posts:
        post_meta[each] = get_post_metadata(each)
    del posts
    if method is True:
        keys = list(post_meta.keys())
        for each in keys:
            # normally we can just iterate over the dict, but we want to avoid an
            # an error so we don't do that here.
            if not common.contents_in_array(tags, post_meta[each]["TAGS"]):
                del post_meta[each]
    elif method is None:
        output = {}
        keys = list(post_meta.keys())
        for each in keys:
            # normally we can just iterate over the dict, but we want to avoid an
            # an error so we don't do that here.
            for each1 in tags:
                if tags[each1] in post_meta[each]["TAGS"]:
                    output[each] = post_meta[each]
                    break
        post_meta = output
    elif method is False:
        keys = list(post_meta.keys())
        for each in keys:
            # normally we can just iterate over the dict, but we want to avoid an
            # an error so we don't do that here.
            if common.contents_in_array(tags, post_meta[each]["TAGS"]):
                del post_meta[each]
    return post_meta


def get_raw_post(title):
    """Get a raw markdown post, based on title"""
    path = f"posts/wiki/{title}.md"
    if os.path.exists(path):
        with open(path, "r") as file:
            content = file.read()
    else:
        raise FileNotFoundError(f"{path} not found")
    metadata = get_post_metadata(title)
    # return combined data
    data = {"metadata": metadata, "content": content}
    return data


def get_isolated_post(title):
    """Get a post, outside of it's web page wrapper"""
    data = get_raw_post(title)
    data["content"] = markdown.markdown(data["content"])
    return data


def get_post(title):
    """Get a post, inside it's web page wrapper

    This includes time formatting, and any sort of further parsing.
    """
    data = get_isolated_post(title)
    data["content"] = data["content"].split("\n")
    data["content"][1] = "\n".join(data["content"][1:])
    data["content"] = data["content"][:2]
    data["content"][0] = data["content"][0][4:-5]
    post = render_template("wiki-post.html")
    post = post.split("{ title }")
    post.insert(1, data["content"][0])
    post = "\n".join(post)
    post = post.split("{ content }")
    post.insert(1, data["content"][1])
    data["content"] = "\n".join(post)
    return data["content"]


def get_all_tags():
    """Get a list of all tags"""
    posts = list_posts()
    for each in enumerate(posts):
        posts[each[0]] = get_post_metadata(each[1])["TAGS"]
    tags = []
    for each in posts:
        tags = tags + each
    del posts
    tags = common.unique(tags)
    return tags


def search_freetext(text, posts):
    """Search synopsis and text of all posts for posts with a
    certain number of matches
    """
    # get our posts pre-transcoding
    post_data = {}
    for each in posts:
        post_data[each] = get_raw_post(each)
        post_data[each]["synopsis_count"] = 0
        post_data[each]["post_count"] = 0
        post_data[each]["title_count"] = 0
    # filter each post
    for each in list(post_data.keys()):
        # filter for each search term
        for each1 in text:
            post_data[each]["synopsis_count"] += post_data[each]["metadata"]["SYNOPSIS"].count(each1)
            post_data[each]["post_count"] += post_data[each]["content"].count(each1)
            post_data[each]["title_count"] += each.count(each1)
    for each in post_data:
        post_data[each] = post_data[each]["synopsis_count"] + post_data[each]["post_count"] + post_data[each]["title_count"]
    output = []
    for each in post_data:
        if post_data[each] >= common.settings["freetext-match-threshold"]:
            output.append(each)
    return output
