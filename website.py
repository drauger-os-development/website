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
import flask
import urllib3
import wiki
import sys

APP = flask.Flask(__name__)


@APP.route("/")
def main():
    """Handle the root directory of the website"""
    return flask.render_template("index.html")


@APP.route("/download")
def download():
    """3D printing stuffs"""
    return flask.render_template("download.html")


@APP.route("/about")
def about():
    """Disaplay about us page"""
    return flask.render_template("about.html")


def convert_to_html_list(obj):
    """Convert a Python 1D list to an HTML unordered list"""
    output = ""
    for each in obj:
        output = output + f"<li>{each}</li>\n"
    return output


@APP.route("/contact")
@APP.route("/contact_us")
@APP.route("/contact-us")
def contact():
    """Cause I'm a nerd on multiple levels"""
    return flask.render_template("contact.html")


@APP.route("/thank_you")
def thank_you():
    """Cause I'm a nerd on multiple levels"""
    return flask.render_template("thank_you.html")


@APP.route("/system_requirements")
@APP.route("/sys_reqs")
def sys_reqs():
    """Cause I'm a nerd on multiple levels"""
    return flask.render_template("sys_reqs.html")


@APP.route("/contribute")
@APP.route("/contributing")
def contributing():
    """Cause I'm a nerd on multiple levels"""
    return flask.render_template("contributing.html")


@APP.route("/contributors")
def contributors():
    """Cause I'm a nerd on multiple levels"""
    return flask.render_template("contributors.html")


@APP.route("/thank_you_old")
def thank_you_old():
    """Cause I'm a nerd on multiple levels"""
    return flask.render_template("thank_you_old.html")


@APP.route("/assets/<path:path>")
def static_dir(path):
    """Handle asset requests"""
    if ".." in path:
        return flask.redirect(flask.url_for("forbidden"))
    return flask.send_from_directory("assets", path)


@APP.errorhandler(404)
def error_404(e):
    """Catch Error 404"""
    return page_not_found()


@APP.errorhandler(403)
def error_403(e):
    """Catch Error 403"""
    return forbidden()


@APP.errorhandler(418)
def error_418(e):
    """Catch Error 418 (Should never happen)"""
    return i_am_a_teapot()


@APP.errorhandler(500)
def error_500(e):
    """Catch Error 500"""
    return internal_error()


@APP.route("/404")
def page_not_found():
    """Error 404 Page"""
    return flask.render_template('404.html'), 404


@APP.route("/403")
def forbidden():
    """Error 403 Page"""
    return flask.render_template('403.html'), 403

@APP.route("/418")
def i_am_a_teapot():
    """Error 418 Easter Egg Page"""
    return flask.render_template('418.html'), 418

@APP.route("/500")
def internal_error():
    """Error 500 Page"""
    return flask.render_template('500.html'), 500


@APP.route("/go/<path:path>")
def go_path_redirector(path):
    """redirect old /go style links"""
    return flask.redirect(f"https://draugeros.org/{ path }")


@APP.route("/go")
@APP.route("/go/")
def go_path_redirector_backup():
    """redirect old /go style links"""
    return flask.redirect("https://draugeros.org")


@APP.route("/favicon.ico")
def favicon():
    """Provide Favicon"""
    return static_dir("images/favicon.png")


@APP.route("/wiki")
def wiki_homepage(show=None):
    """This is be the wiki homepage and search

    if show is None, then wiki shows the 10 most recent posts
    otherwise, show should be a list of post titles

    if show is not None, a list
    """
    posts_template = """<a href="/wiki/{ title }"><h2>{ title }</h2></a>
<h4>Written { written } by { author }</h4>
<p>{ synopsis }</p>
</br>"""
    tags_template = '<input type="checkbox" style="font-size: var(--nav-summary-tittle-size);margin: 8px 0px" name="%s" value="1"> %s'
    if show is None:
        posts = wiki.list_posts()[:10]
    else:
        if isinstance(show, (list, tuple)):
            posts = show
        else:
            raise TypeError(f"{ show } is not None, a list, or a tuple.")
    tags = wiki.get_all_tags()
    posts_parse_in = []
    for each in posts:
        post = wiki.get_post_metadata(each)
        new = posts_template.replace("{ title }", each)
        new = new.replace("{ written }", post["WRITTEN"])
        new = new.replace("{ synopsis }", post["SYNOPSIS"])
        if "EDITOR" in post:
            new = new.replace("{ author }",
                              f"""{ ', '.join(post['AUTHOR']) }, Edited by { ', '.join(post['EDITOR']) }""")
        else:
            new = new.replace("{ author }", ", ".join(post["AUTHOR"]))
        posts_parse_in.append(new)

    # generate tags search GUI
    tags_parse_in = []
    for each in tags:
        tags_parse_in.append(tags_template % (each, each))

    # make each element
    count = 0
    row_width = 2
    tags_gui = []
    add = []
    for each in tags_parse_in:
        entry = f" <td> { each } </td> "
        if count < row_width:
            add.append(entry)
            count += 1
        else:
            tags_gui.append(add)
            add = []
            add.append(entry)
            count = 1
    if add:
        tags_gui.append(add)

    # combine elements into rows
    newline = "\n" # it is entirely ridiculous that I have to do this due to a SyntaxError
    for each in enumerate(tags_gui):
        tags_gui[each[0]] = f"<tr>{ newline.join(each[1]) }</tr>"

    # combine rows into table
    tags_gui = f"""<table>{ newline.join(tags_gui) }</table>"""

    # parse post previews into page
    if len(posts_parse_in) > 0:
        posts_parse_in = "\n</br>\n".join(posts_parse_in)
        page = flask.render_template("wiki-home.html")
        page = page.replace("{ content }", posts_parse_in)
    else:
        page = flask.render_template("wiki-home-none.html")

    # parse tag info into page
    page = page.replace("{ tags }", tags_gui)
    page = page.replace("{ tags_list }",
                        f"""<input type="hidden" id="tags_list" name="tags_list" value="{ ",".join(tags) }">""")

    # send the page to the user
    return page


def get_tag_method(form):
    """Get tag search method"""
    if form.get("state-g") == "true":
        return True
    elif form.get("state-g") == "false":
        return False
    return None


@APP.route("/wiki/search", methods=["POST"])
def wiki_search():
    """Search the wiki"""
    tags_list = flask.request.form.get("tags_list").split(",")
    tag_search_method = get_tag_method(flask.request.form)
    print(tag_search_method)
    if tags_list is not None:
        tags = {}
        for each in tags_list:
            tags[each] = bool(flask.request.form.get(each))
        for each in range(len(tags_list) - 1, -1, -1):
            if not tags[tags_list[each]]:
                del tags_list[each]
        del tags
        output = list(wiki.search_tags(tags_list,
                                       method=tag_search_method).keys())
    else:
        output = wiki.list_posts()
    search_text = flask.request.form.get("free_text").split(" ")
    output = wiki.search_freetext(search_text, output)
    return wiki_homepage(show=output)


@APP.route("/wiki/<title>")
def wiki_post(title):
    """Provide rendered wiki posts"""
    try:
        return wiki.get_post(title)
    except FileNotFoundError:
        return page_not_found()


@APP.route("/privacy")
def privacy():
    """Provide the user with our privacy policy"""
    http = urllib3.PoolManager()
    # download markdown-formatted Privacy Policy from our GitHub
    data = http.request("GET",
                        "https://raw.githubusercontent.com/drauger-os-development/Policies-and-Operations-Manual/master/Privacy%20Policy.md").data
    data = data.decode()
    data = wiki.render_post(data)
    return data


@APP.route("/tos")
def tos():
    """Provide the user with our Terms of Service"""
    http = urllib3.PoolManager()
    # download markdown-formatted Terms of Service from our GitHub
    data = http.request("GET",
                        "https://raw.githubusercontent.com/drauger-os-development/Policies-and-Operations-Manual/master/Terms%20of%20Service.md").data
    data = data.decode()
    data = wiki.render_post(data)
    return data


if __name__ == "__main__":
    if ("--debug" in sys.argv) or ("-debug" in sys.argv) or ("-d" in sys.argv):
        mode=True
    else:
        mode=False
    APP.run(host="0.0.0.0", debug=mode)
