#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  personal_website.py
#
#  Copyright 2021 Thomas Castleman <contact@draugeros.org>
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
"""This is my personal website"""
from flask import Flask, render_template
import json

APP = Flask(__name__)


@APP.route("/")
def main():
    """Handle the root directory of the website"""
    return render_template("index.html")


@APP.route("/3d-printing")
def three_d():
    """3D printing stuffs"""
    return render_template("3d.html")


@APP.route("/anime")
def anime():
    """A Weeb's favorite pass time"""
    with open("anime.json", "r") as file:
        data = json.load(file)
    watched = convert_to_html_list(data["Watched"])
    watching = convert_to_html_list(data["Watching"])
    on_hold = convert_to_html_list(data["On Hold"])
    ptw = convert_to_html_list(data["To Watch"])
    output = render_template("anime.html", on_hold=on_hold, to_watch=ptw,
                             watched=watched, watching=watching)
    output = output.replace("&lt;", "<")
    output = output.replace("&gt;", ">")
    return output

def convert_to_html_list(obj):
    """Convert a Python 1D list to an HTML unordered list"""
    output = ""
    for each in obj:
        output = output + f"<li>{each}</li>\n"
    return output

@APP.route("/software")
def software():
    """Cause I'm a nerd on multiple levels"""
    return render_template("software.html")


@APP.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    APP.run(host="0.0.0.0", debug=False)
