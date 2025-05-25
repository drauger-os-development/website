#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  website.py
#
#  Copyright 2023 Thomas Castleman <contact@draugeros.org>
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
import time
import common

START_TIME = time.time()
APP = flask.Flask(__name__)


@APP.route("/")
def main():
    """Handle the root directory of the website"""
    return flask.render_template("index.html", master_title="Drauger OS - Home",
                                 master_desc="Drauger OS is an open-source desktop Linux gaming OS.",
                                 author="",
                                 seo_keywords=", ".join(common.seo_keywords))


@APP.route("/download")
def download():
    """Download the ISO"""
    return flask.render_template("download.html", master_title="Drauger OS - Download",
                                 master_desc="Download Drauger OS, the open-source desktop Linux gaming OS.",
                                 author="",
                                 seo_keywords=", ".join(common.seo_keywords + ["download"]))


@APP.route("/about")
def about():
    """Disaplay about us page"""
    return flask.render_template("about.html", master_title="Drauger OS - About",
                                 master_desc="All about Drauger OS, the open-source desktop Linux gaming OS.",
                                 author="Thomas Castleman",
                                 seo_keywords=", ".join(common.seo_keywords + ["about"]))


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
    """Contact page"""
    return flask.render_template("contact.html", master_title="Drauger OS - Contact Us",
                                 master_desc="Contact the Drauger OS Team",
                                 author="Thomas Castleman",
                                 seo_keywords=", ".join(common.seo_keywords + ["contact us", "contact"]))


@APP.route("/thank_you")
def thank_you():
    """Thank the users for downloading the OS"""
    return flask.render_template("thank_you.html", master_title="Drauger OS - Thank You",
                                 master_desc="Thank you for downloading Drauger OS!",
                                 author="",
                                 seo_keywords=", ".join(common.seo_keywords + ["download"]))


@APP.route("/system_requirements")
@APP.route("/sys_reqs")
def sys_reqs():
    """System Requirements"""
    return flask.render_template("sys_reqs.html", master_title="Drauger OS - System Requirements",
                                 master_desc="System Requirements for Drauger OS",
                                 author="Thomas Castleman",
                                 seo_keywords=", ".join(common.seo_keywords + ["system requirements", "sys reqs", "requirements", "hardware requirements"]))


@APP.route("/contribute")
@APP.route("/contributing")
def contributing():
    """How to Contribute"""
    return flask.render_template("contributing.html", master_title="Drauger OS - Contributing",
                                 master_desc="How to contribute to Drauger OS",
                                 author="Thomas Castleman",
                                 seo_keywords=", ".join(common.seo_keywords + ["contributing"]))


@APP.route("/contributors")
def contributors():
    """Honor our contributors"""
    return flask.render_template("contributors.html", master_title="Drauger OS - Contributors",
                                 master_desc="Contributors to Drauger OS",
                                 author="Thomas Castleman",
                                 seo_keywords=", ".join(common.seo_keywords))


@APP.route("/thank_you_beta")
def thank_you_beta():
    """Thank users for downloading the OS, beta version"""
    return flask.render_template("thank_you_beta.html", master_title="Drauger OS - Thank You",
                                 master_desc="Thank you for Downloading Drauger OS - BETA VERSION",
                                 author="",
                                 seo_keywords=", ".join(common.seo_keywords + ["download"]))


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
    return flask.render_template('404.html', master_title="Drauger OS - 404",
                                 master_desc="Error 404",
                                 author="",
                                 seo_keywords=", ".join(common.seo_keywords)), 404


@APP.route("/403")
def forbidden():
    """Error 403 Page"""
    return flask.render_template('403.html', master_title="Drauger OS - 403",
                                 master_desc="Error 403",
                                 author="",
                                 seo_keywords=", ".join(common.seo_keywords)), 403


@APP.route("/418")
def i_am_a_teapot():
    """Error 418 Easter Egg Page"""
    return flask.render_template('418.html', master_title="Drauger OS - 418",
                                 master_desc="Error 418",
                                 author="",
                                 seo_keywords=", ".join(common.seo_keywords)), 418


@APP.route("/500")
def internal_error():
    """Error 500 Page"""
    return flask.render_template('500.html', master_title="Drauger OS - 500",
                                 master_desc="Error 500",
                                 author="",
                                 seo_keywords=", ".join(common.seo_keywords)), 500


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


@APP.route("/robots.txt")
def robot_txt():
    """Provide robots.txt"""
    return static_dir("etc/robots.txt")


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
        page = flask.render_template("wiki-home.html", master_title="Drauger OS Wiki - Home",
                                 master_desc="The Drauger OS Wiki is here to help you fix issues with your Drauger OS installation, or help you contribute to the community!",
                                 author="",
                                 seo_keywords=", ".join(common.seo_keywords + ["wiki", "help", "support", "issues", "issue"]))
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
@APP.route("/privacy-policy")
@APP.route("/privacy_policy")
@APP.route("/privacy policy")
def privacy():
    """Provide the user with our privacy policy"""
    http = urllib3.PoolManager()
    # download markdown-formatted Privacy Policy from our GitHub
    data = http.request("GET",
                        "https://raw.githubusercontent.com/drauger-os-development/Policies-and-Operations-Manual/master/Privacy%20Policy.md").data
    data = data.decode()
    data = wiki.render_post(data, desc="The Drauger OS Privacy Policy",
                            tags=["privacy", "privacy policy",
                                  "personal data"],
                            author="Drauger OS Core Contributor Team")
    return data


@APP.route("/tos")
def tos():
    """Provide the user with our Terms of Service"""
    http = urllib3.PoolManager()
    # download markdown-formatted Terms of Service from our GitHub
    data = http.request("GET",
                        "https://raw.githubusercontent.com/drauger-os-development/Policies-and-Operations-Manual/master/Terms%20of%20Service.md").data
    data = data.decode()
    data = wiki.render_post(data, desc="The Drauger OS Terms of Service",
                            tags=["tos", "terms of service",
                                  "service"],
                            author="Drauger OS Core Contributor Team")
    return data


@APP.route("/community-guidelines")
@APP.route("/community_guidelines")
@APP.route("/community guidelines")
def guidelines():
    """Provide the user with our Terms of Service"""
    http = urllib3.PoolManager()
    # download markdown-formatted Terms of Service from our GitHub
    data = http.request("GET",
                        "https://raw.githubusercontent.com/drauger-os-development/Policies-and-Operations-Manual/master/Community%20Guidelines.md").data
    data = data.decode()
    data = wiki.render_post(data, desc="The Drauger OS Community Guidelines",
                            tags=["community", "guidelines",
                                  "community guidelines", "ethics policy"],
                            author="Drauger OS Core Contributor Team")
    return data


@APP.route("/up")
@APP.route("/status")
def check_up():
    """Respond for whether website is up so response can be more easily checked programmatically"""
    global START_TIME
    return {"status": True,
            "START_TIME": START_TIME}


if __name__ == "__main__":
    if ("--debug" in sys.argv) or ("-debug" in sys.argv) or ("-d" in sys.argv):
        mode=True
    else:
        mode=False
    APP.run(host="0.0.0.0", debug=mode)
