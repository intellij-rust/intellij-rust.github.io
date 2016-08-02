---
title: FAQ
order: 999999
---

{% include h title="Are you going to use racer or RLS?" tag="racer" %}

No, we plan to implement most of the language analysis from scratch. This is
a lot of work, but the benefits are substantial. We would be able to leverage
IntelliJ Platform infrastructure for incremental analysis and indexing. With
our own analysis we can provide more flexible quick fixes, intentions and typing
assistance.

The same applies to the formatter (that is also from scratch, but we plan to
support running `rustfmt` as an action). It is necessary for proper working
of almost any feature which is modifying source code.

{% include h title="Does IntelliJ Rust have a debugger?" tag="racer" %}

There is no debugger support at the moment. It will be implemented eventually,
but there is no precise plan now. You may want to subscribe/vote on [this issue][debugger].

[debugger]: https://github.com/intellij-rust/intellij-rust/issues/535
