---
title: Troubleshooting
---

{% include doc-shortcut-tip.html %}

{% include h title="Are you experiencing problems after update?" %}

In general, plugin updates should go smoothly. Though, if you experience some
weird behavior, try reimporting your project or/and rebuilding indices (using
**Invalidate caches/Restart** action). Previous versions are available at
[https://plugins.jetbrains.com/plugin/8182](https://plugins.jetbrains.com/plugin/8182).


{% include h title="Is Cargo project structure correct?" %}

At the moment we support only Cargo based projects. Check that `Cargo.toml` is
present in the root directory of the project and that you can build the project
with `cargo build`. You can use `cargo metadata` command to understand how
exactly IntelliJ Rust sees your project.


{% include h title="Is the Rust toolchain properly setup?" %}

Check `Settings > Languages & Frameworks > Rust` to see if paths to `cargo`,
`rustc` and standard library are set up correctly.


{% include h title="Do IntelliJ Rust and Cargo work together?" %}

Invoke **Refresh Cargo project** action to force IntelliJ Rust to update Cargo
related project info. You should see a notification about successful update.


{% include h title="Maybe it is a bug?" %}

If neither of these tips helped you, do not hesitate to file an [issue] on our
bugtracker or ping us on our [chat].


[issue]: https://github.com/intellij-rust/intellij-rust/issues
[chat]: https://gitter.im/intellij-rust/intellij-rust
[Cargo]: http://doc.crates.io/guide.html
