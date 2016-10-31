---
title: FAQ
order: 999999
---

{% include h title="Where is Rust SDK?" tag="sdk" %}

We don't use IntelliJ IDEA's SDK concept to manage Rust versions because it is
specific to IDEA and is not present, for example, in the CLion. Path to Cargo is
configured per project in the `Settings > Languages & Frameworks > Rust`.

{% include h title="Why Make Project action does not work?" tag="make" %}

Because we don't use an SDK, the generic **Make Project** action is not
available. Instead, you can create a **Run Configuration** with a `cargo build`
command. That way, you can also specify necessary Cargo flags, like
`--features`.

{% include h title="Does IntelliJ Rust have a debugger?" tag="debugger" %}

There is no debugger support at the moment. It will be implemented eventually,
but there is no precise plan now. You may want to subscribe/vote on [this issue][debugger].


{% include h title="Are you going to use racer or RLS?" tag="racer" %}

No, we plan to implement most of the language analysis from scratch. This is
a lot of work, but the benefits are substantial. We would be able to leverage
IntelliJ Platform infrastructure for incremental analysis and indexing. With
our own analysis we can provide more flexible quick fixes, intentions and typing
assistance.

The same applies to the formatter (that is also from scratch, but we plan to
support running `rustfmt` as an action). It is necessary for proper working
of almost any feature which is modifying source code.


[debugger]: https://github.com/intellij-rust/intellij-rust/issues/535
