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
import markdown
import os
from flask import render_template
import json
import time

# load our settings globally
with open("settings.json", "r") as file:
    settings = json.load(file)


def list_posts():
    """List all available posts"""
    return os.listdir("post-meta/wiki")


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
                                              settings["time-format-stored"])
        else:
            metadata[data[0].upper()] = data[1]
    keys = ["SYNOPSIS" , "TAGS", "AUTHOR", "WRITTEN"]
    metadata["WRITTEN"] = time.strftime(settings["time-format-displayed"], metadata["WRITTEN"])
    if not all(item in metadata.keys() for item in keys):
        raise TypeError(f"Not all fields of { keys } in { path }")
    return metadata


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
