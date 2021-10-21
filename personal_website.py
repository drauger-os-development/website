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

APP = Flask(__name__)


@APP.route("/")
def main():
    """Handle the root directory of the mirrors"""
    return render_template("index.html")


if __name__ == "__main__":
    APP.run(host="0.0.0.0", debug=False)
