#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  db.py
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
"""Explain what this program does here!!!"""
import sqlite3 as sql
import json
import os


with open("db-settings.json", "r") as file:
    settings = json.load(file)


def get_db_files():
    """return available db files"""
    return settings["db-files"]


def get_db_connection(file_name: str):
    """Get database connection for a valid, allowed database

    raise FileNotFoundError if db is allowed but not found.
    raise NameError if db is not allowed
    """
    if file_name in settings["db-files"]:
        if os.path.isfile(file_name):
            return sql.connect(file_name)
        raise FileNotFoundError(f"{file_name} not found on file system")
    raise NameError(f"{file_name} not a valid database")


def get_db_tables(file_name: str, db):
    """Get approved tables in database"""
    tables = db.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = tables.fetchall()[0]
    if file_name in settings["db-files"]:
        expected_tables = list(settings[file_name].keys())
        for each in range(len(tables) - 1, -1, -1):
            if tables[each] not in expected_tables:
                del tables[each]
        return expected_tables
    raise NameError(f"{file_name} not a valid database")


def get_all_entries(table: str, db):
    """Get all entries in a table"""
    command = f"SELECT * FROM {table}"
    data = db.execute(command).fetchall()
    return data


def tags_search(tags: (list, tuple), table: str, db, method=True):
    """Search for entries which match a given tag or tags

    method can be one of 3 values: True, False, or None

    if method == True, entry must have ALL tags. This is the default behavior.
    if method == False, entry must have NONE of tags.
    if method == None, entry may have one or more of tags.
    """
    # this needs to be fleshed out
    command = f"SELECT * FROM {table} WHERE tags like "
    if not isinstance(tags, (list, tuple)):
        raise TypeError(f"{tags} is not of type list or tuple")
    entries = []
    # figure out how to search in the 3 optional ways
    return entries

