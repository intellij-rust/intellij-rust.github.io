---
title: FAQ
order: 999999
---

{% include h title="Where is the Rust SDK?" tag="sdk" %}

We don't use IntelliJ IDEA's SDK concept to manage Rust versions because it is
specific to IDEA and is not present, for example, in CLion. The path to Cargo is
configured per project through `Settings > Languages & Frameworks > Rust`.

{% include h title="Does IntelliJ Rust have a debugger?" tag="debugger" %}

There is preliminary debugger support for CLion, see [this issue][debugger] for
details.

{% include h title="Are you going to use racer or RLS?" tag="racer" %}

No, we plan to implement most of the language analysis from scratch. This is
a lot of work, but the benefits are substantial. We would be able to leverage
the IntelliJ Platform infrastructure for incremental analysis and indexing. With
our analysis, we can provide more flexible quick fixes, intentions and typing
assistance.

The same applies to the formatter (that is also from scratch, but we plan to
support running `rustfmt` as an action). It is necessary for proper working
of almost any feature which is modifying source code.


[debugger]: https://github.com/intellij-rust/intellij-rust/issues/535
