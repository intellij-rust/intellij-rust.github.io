#!/usr/bin/env python3
import argparse
import datetime
import os
import re
import urllib.request
from dataclasses import dataclass
from typing import Set, List, Optional, Dict, TextIO

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
    "amakeev",
    "MarinaKalashina",
    "dima74",
    "avrong"
]


@dataclass
class ChangelogItem:
    pull_request_id: int
    description: str
    username: str

    def display(self):
        if self.username in MAINTAINERS:
            return "<!-- https://github.com/intellij-rust/intellij-rust/pull/{} -->\n* {}"\
                .format(self.pull_request_id, self.description)
        else:
            return "<!-- https://github.com/intellij-rust/intellij-rust/pull/{} -->\n* {} (by [@{}])"\
                .format(self.pull_request_id, self.description, self.username)


class ChangelogSection(object):
    header: str
    items: List[ChangelogItem]

    def __init__(self, header: str):
        self.header = header
        self.items = []

    def add_item(self, item: ChangelogItem):
        self.items.append(item)

    def display(self):
        return """## {}\n\n""".format(self.header) + "\n\n".join(map(lambda l: l.display(), self.items))


class Changelog(object):
    labels: List[str]
    sections: Dict[str, ChangelogSection]
    contributors: Set[str]
    milestone_id: Optional[int]

    def __init__(self, milestone_id=None):
        self.milestone_id = milestone_id
        self.labels = []
        self.sections = {}
        self.contributors = set()
        self.__add_section("feature", ChangelogSection("New Features"))
        self.__add_section("performance", ChangelogSection("Performance Improvements"))
        self.__add_section("fix", ChangelogSection("Fixes"))
        self.__add_section("internal", ChangelogSection("Internal Improvements"))

    def __add_section(self, label: str, section: ChangelogSection):
        self.labels.append(label)
        self.sections[label] = section

    def add_item(self, label: str, item: ChangelogItem):
        section = self.sections.get(label)
        if section is not None:
            section.add_item(item)
            if item.username not in MAINTAINERS:
                self.contributors.add(item.username)

    def write(self, f: TextIO):
        for label in self.labels:
            section = self.sections[label]
            if section.items:
                f.write(section.display())
                f.write("\n\n")
        if self.milestone_id is not None:
            f.write("Full set of changes can be found [here]"
                    "(https://github.com/intellij-rust/intellij-rust/milestone/{}?closed=1)\n"
                    .format(self.milestone_id))

        if len(self.contributors) > 0:
            f.write("\n")
            sorted_contributors = sorted(self.contributors)
            for name in sorted_contributors:
                url = contributor_url(name)
                f.write(url)


def collect_changelog(repo: Repository, milestone: Milestone):
    print(f"Collecting changelog issues for `{milestone.title}` milestone")

    changelog = Changelog(milestone.number)
    issues = repo.get_issues(milestone=milestone, state="all")

    comment_pattern = re.compile("<!--.*-->", re.RegexFlag.DOTALL)
    changelog_description_pattern = re.compile("changelog:(?P<description>([^\n]+\n?)*)")
    for issue in issues:
        if issue.pull_request is None:
            continue
        labels: Set[str] = set(map(lambda l: l.name, issue.labels))
        if len(labels) == 0:
            continue

        issue_text = re.sub(comment_pattern, "", issue.body).replace("\r\n", "\n")
        result = re.search(changelog_description_pattern, issue_text)
        if result is not None:
            description = result.group("description").strip()
        else:
            description = issue.title
        changelog_item = ChangelogItem(issue.number, description, issue.user.login)
        for label in labels:
            changelog.add_item(label, changelog_item)

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
    date = datetime.datetime.now()

    changelog = Changelog()
    if not args.offline:
        if args.token is not None:
            login_or_token = args.token
            password = None
        else:
            login_or_token = args.login
            password = args.password

        expected_milestone_title = f"v{next_post}"
        g = Github(login_or_token, password)
        repo: Repository = g.get_repo("intellij-rust/intellij-rust")

        milestone: Optional[Milestone] = None
        for m in repo.get_milestones():
            if m.title == expected_milestone_title:
                milestone = m
                break

        if milestone is None:
            raise RuntimeError(f"Milestone `{expected_milestone_title}` is not found")

        due_on = milestone.due_on
        if due_on is not None:
            date = due_on.replace(hour=17, minute=0, second=0)  # 17:00 is our usual release time
        changelog = collect_changelog(repo, milestone)

    name = "_posts/{}-changelog-{}.markdown".format(date.date().isoformat(), next_post)

    with open(name, 'w') as f:
        f.write("""---
layout: post
title: "IntelliJ Rust Changelog #{}"
date: {}
---


""".format(next_post, date.strftime("%Y-%m-%d %H:%M:%S +0300")))

        changelog.write(f)


def contributors():
    last_post = "_posts/" + sorted(os.listdir("_posts"))[-1]

    with open(last_post) as f:
        text = f.read()

    names = sorted({n[2:-1] for n in re.findall(r"\[@[^]]+]", text)})

    with open(last_post) as f:
        old_text = f.read()

    with open(last_post, 'a') as f:
        f.write("\n")
        for name in names:
            line = contributor_url(name)
            if line not in old_text:
                f.write(line)


def contributor_url(username: str):
    url = "https://github.com/" + username
    print("checking " + url)
    req = urllib.request.Request(url, method="HEAD")
    with urllib.request.urlopen(req) as _:
        pass  # will thrown on 404

    line = "[@{}]: {}\n".format(username, url)
    return line


if __name__ == '__main__':
    main()
