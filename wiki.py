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


def get_raw_post(title):
    """Get a raw markdown post, based on title"""
    path = f"posts/wiki/{title}.md"
    if os.path.exists(path):
        print("File found!")
        with open(path, "r") as file:
            content = file.read()
        print("File read!")
        return content
    else:
        raise FileNotFoundError(f"{path} not found")


def get_isolated_post(title):
    """Get a post, outside of it's web page wrapper"""
    content = get_raw_post(title)
    content = markdown.markdown(content)
    return content


def get_post(title):
    """Get a post, inside it's web page wrapper"""
    content = get_isolated_post(title)
    content = content.split("\n")
    content[1] = "\n".join(content[1:])
    content = content[:2]
    content[0] = content[0][4:-5]
    post = render_template("wiki-post.html")
    post = post.split("{ title }")
    post.insert(1, content[0])
    post = "\n".join(post)
    post = post.split("{ content }")
    post.insert(1, content[1])
    content = "\n".join(post)
    return content
