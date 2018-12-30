#!/usr/bin/env python3
import argparse
import datetime
import itertools
import os
import re
import urllib.request
from dataclasses import dataclass
from typing import Set, List

from github import Github
from github.GitCommit import GitCommit
from github.Repository import Repository

MERGE_REGEX = re.compile(r"Merge #(\d+)")
MAINTAINERS = [
    "matklad",
    "Undin",
    "vlad20012",
    "mchernyavsky",
    "ortem",
    "amakeev"
]


@dataclass
class ChangelogItem:
    title: str
    username: str

    def display(self):
        if self.username in MAINTAINERS:
            return "* {}".format(self.title)
        else:
            return "* {} (by [@{}])".format(self.title, self.username)


class Changelog:
    features: List[ChangelogItem] = []
    fixes: List[ChangelogItem] = []
    internals: List[ChangelogItem] = []

    def __repr__(self):
        return "features:\n{}\n\nfixes:\n{}\n\ninternals:\n{}\n".format(self.features, self.fixes, self.internals)

    def add_feature(self, feature: ChangelogItem):
        self.features.append(feature)

    def add_fix(self, fix: ChangelogItem):
        self.fixes.append(fix)

    def add_internal(self, internal: ChangelogItem):
        self.internals.append(internal)


def collect_changelog(login_or_token: str, password: str = None):
    print("checking repo commits")
    changelog = Changelog()
    g = Github(login_or_token, password)
    repo: Repository = g.get_repo("intellij-rust/intellij-rust")
    commits = repo.get_commits()

    for page_number in itertools.count():
        print("checking commit page {}".format(page_number))
        page = commits.get_page(page_number)
        for commit in page:
            git_commit: GitCommit = commit.commit
            message: str = git_commit.message

            if message == "Changelog":
                return changelog

            if len(commit.parents) == 1:
                # we want to check only merge commits
                continue

            first_line: str = message.splitlines()[0]
            result = re.match(MERGE_REGEX, first_line)
            if result is None:
                continue
            pull_request_id = int(result[1])
            pull_request = repo.get_pull(pull_request_id)
            labels: Set[str] = set(map(lambda l: l.name, pull_request.labels))

            changelog_item = ChangelogItem(pull_request.title, pull_request.user.login)
            if "feature" in labels:
                changelog.add_feature(changelog_item)
            if "fix" in labels:
                changelog.add_fix(changelog_item)
            if "internal" in labels:
                changelog.add_internal(changelog_item)
    return changelog


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", action='store_true', help="add contributor links")
    parser.add_argument("--offline", action='store_true', help="do not preform net requests")
    parser.add_argument("--token", type=str, help="github token")
    parser.add_argument("--login", type=str, help="github login")
    parser.add_argument("--password", type=str, help="github password")

    args = parser.parse_args()

    if args.c:
        contributors()
    else:
        new_post(args)


def new_post(args: argparse.Namespace):
    next_post = len(os.listdir("_posts"))
    today = datetime.date.today().isoformat()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S +0300")
    name = "_posts/{}-changelog-{}.markdown".format(today, next_post)

    changelog = Changelog()
    if not args.offline:
        if args.token is not None:
            login_or_token = args.token
            password = None
        else:
            login_or_token = args.login
            password = args.password
        changelog = collect_changelog(login_or_token, password)
    with open(name, 'w') as f:
        f.write("""---
layout: post
title: "IntelliJ Rust Changelog #{}"
date: {}
---


""".format(next_post, now))

        f.write("""## New Features\n\n""")
        for feature in changelog.features:
            f.write("{}\n\n".format(feature.display()))
        f.write("""## Fixes\n\n""")
        for fix in changelog.fixes:
            f.write("{}\n\n".format(fix.display()))
        f.write("""## Internal Improvements\n\n""")
        for internal in changelog.internals:
            f.write("{}\n\n".format(internal.display()))


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
