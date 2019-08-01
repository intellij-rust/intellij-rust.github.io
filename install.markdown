---
layout: page
title: Install IntelliJ Rust
---

## Alpha builds

IntelliJ Rust is in _alpha_ stage. We regularly publish stable builds to the JetBrains plugin [repository](https://plugins.jetbrains.com/plugin/8182).
You can download and install these builds directly from `Settings / Preferences | Plugins | Marketplace` in your IDE.

For bug reports and feature requests, please use our [issue tracker](https://github.com/intellij-rust/intellij-rust/issues).

## Nightly builds

In addition to aplha releases, we also ship pre-builds of _intellij-rust_ and _intellij-toml_ in the nightly channel.

To use them, follow this
[instruction](https://www.jetbrains.com/idea/help/managing-enterprise-plugin-repositories.html#repos)
for adding a custom plugin repository, and use one of the following URLs:

```yaml
- Rust: https://plugins.jetbrains.com/plugins/nightly/8182
- TOML: https://plugins.jetbrains.com/plugins/nightly/8195
```

Nightly builds are daily snapshots of the current development branch, so there may be more bugs than in the alpha channel. If you find one, please file an
[issue](https://github.com/intellij-rust/intellij-rust/issues) in our tracker.

## Compatible IDEs

The plugin is compatible with all Intellij-based IDEs like IDEA, CLion, or PyCharm. The latest plugin version supports the latest released platform version (for example, `2019.2`).
