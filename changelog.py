#!/usr/bin/env python3
import argparse
import datetime
import os
import re
import urllib.request
from dataclasses import dataclass
from typing import Set, List

# https://github.com/PyGithub/PyGithub
from github import Github
from github.Milestone import Milestone
from github.Repository import Repository

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
    pull_request_id: int
    title: str
    username: str

    def display(self):
        if self.username in MAINTAINERS:
            return "<!-- https://github.com/intellij-rust/intellij-rust/pull/{} -->\n* {}"\
                .format(self.pull_request_id, self.title)
        else:
            return "<!-- https://github.com/intellij-rust/intellij-rust/pull/{} -->\n* {} (by [@{}])"\
                .format(self.pull_request_id, self.title, self.username)


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


def collect_changelog(post_number: int, login_or_token: str, password: str = None):
    expected_milestone_title = f"v{post_number}"
    print(f"Collecting changelog issues for `{expected_milestone_title}` milestone")
    changelog = Changelog()
    g = Github(login_or_token, password)
    repo: Repository = g.get_repo("intellij-rust/intellij-rust")

    milestone: Milestone = None
    for m in repo.get_milestones():
        if m.title == expected_milestone_title:
            milestone = m
            break

    if milestone is None:
        raise RuntimeError(f"Milestone `{expected_milestone_title}` is not found")

    issues = repo.get_issues(milestone=milestone, state="all")
    for issue in issues:
        if issue.pull_request is None:
            continue
        labels: Set[str] = set(map(lambda l: l.name, issue.labels))
        changelog_item = ChangelogItem(issue.number, issue.title, issue.user.login)
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
        changelog = collect_changelog(next_post, login_or_token, password)
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
