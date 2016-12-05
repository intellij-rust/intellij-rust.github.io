#!/usr/bin/env bash

set -e

next_post=$(ls _posts | wc -l)
today=$(date +"%Y-%m-%d")

cat << EOF > _posts/$today-changelog-$next_post.markdown
---
layout: post
title: "IntelliJ Rust Changelog #$next_post"
date: $(date +"%Y-%m-%d %H:%M:%S %z")
---

## New Features

## Fixes

## Refactorings

[@w]: https://github.com/w
EOF
