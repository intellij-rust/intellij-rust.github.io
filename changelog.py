#!/usr/bin/env python3
import datetime
import os
import re
import sys
import urllib.request


def main():
    if "-c" in sys.argv:
        contributors()
    else:
        new_post()


def new_post():
    next_post = len(os.listdir("_posts"))
    today = datetime.date.today().isoformat()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S +0300")
    name = "_posts/{}-changelog-{}.markdown".format(today, next_post)
    with open(name, 'w') as f:
        f.write("""---
layout: post
title: "IntelliJ Rust Changelog #{}"
date: {}
---


## New Features


## Fixes


## Internal Improvements


""".format(next_post, now))


def contributors():
    last_post = "_posts/" + sorted(os.listdir("_posts"))[-1]

    with open(last_post) as f:
        text = f.read()

    names = sorted({n[2:-1] for n in re.findall(r"\[@[^\]]+\]", text)})

    with open(last_post) as f:
        old_text = f.read()

    with open(last_post, 'a') as f:
        f.write("\n")
        for name in names:
            url = "https://github.com/" + name
            print("checking " + url)
            req = urllib.request.Request(url, method="HEAD")
            with urllib.request.urlopen(req) as _:
                pass  # will thrown on 404

            line = "[@{}]: {}\n".format(name, url)
            if line not in old_text:
                f.write(line)


if __name__ == '__main__':
    main()
