#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  website.py
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
"""Drauger OS website"""
from flask import Flask, render_template, send_from_directory, redirect, url_for
import os
import json

APP = Flask(__name__)


@APP.route("/")
def main():
    """Handle the root directory of the website"""
    return render_template("index.html")


@APP.route("/download")
def download():
    """3D printing stuffs"""
    return render_template("download.html")


@APP.route("/about")
def about():
    """Disaplay about us page"""
    return render_template("about.html")


def convert_to_html_list(obj):
    """Convert a Python 1D list to an HTML unordered list"""
    output = ""
    for each in obj:
        output = output + f"<li>{each}</li>\n"
    return output


@APP.route("/contact")
def contact():
    """Cause I'm a nerd on multiple levels"""
    return render_template("contact.html")


@APP.route("/thank_you")
def thank_you():
    """Cause I'm a nerd on multiple levels"""
    return render_template("thank_you.html")


@APP.route("/system_requirements")
@APP.route("/sys_reqs")
def sys_reqs():
    """Cause I'm a nerd on multiple levels"""
    return render_template("sys_reqs.html")


@APP.route("/contribute")
@APP.route("/contributing")
def contributing():
    """Cause I'm a nerd on multiple levels"""
    return render_template("contributing.html")


@APP.route("/contributors")
def contributors():
    """Cause I'm a nerd on multiple levels"""
    return render_template("contributors.html")


@APP.route("/thank_you_old")
def thank_you_old():
    """Cause I'm a nerd on multiple levels"""
    return render_template("thank_you_old.html")


@APP.route("/assets/<path:path>")
def static_dir(path):
    if ".." in path:
        return redirect(url_for("forbidden"))
    if path not in os.listdir("assets"):
        return redirect(url_for("page_not_found"))
    return send_from_directory("assets", path)


@APP.errorhandler(404)
def error_404(e):
    return page_not_found()


@APP.errorhandler(403)
def error_403(e):
    return forbidden()


@APP.route("/404")
def page_not_found():
    return render_template('404.html'), 404


@APP.route("/403")
def forbidden():
    return render_template('403.html'), 403


@APP.route("/go/<path:path>")
def go_path_redirector(path):
    """redirect old /go style links"""
    return redirect(f"https://draugeros.org/{ path }")


@APP.route("/go")
@APP.route("/go/")
def go_path_redirector_backup():
    """redirect old /go style links"""
    return redirect("https://draugeros.org")


@APP.route("/favicon.ico")
def favicon():
    return static_dir("favicon.png")


if __name__ == "__main__":
    APP.run(host="0.0.0.0", debug=False)
