---
layout: page
title: Install IntelliJ Rust
---

## Getting alpha builds

IntelliJ Rust is currently in the _alpha_ stage of development. When we reach some acceptable level of stability,
we publish alpha builds to the IntelliJ's main plugin [repository](https://plugins.jetbrains.com/plugin/8182).
You can download and install these builds directly from `Plugins > Browse repositories` screen in your IDE.

As this is a preview release, something might go wrong. So, be brave to face some nasty bugs.
If you find one, we would very appreciate if you file an [issue](https://github.com/intellij-rust/intellij-rust/issues)
on our bugtracker or ping us on our [chat](https://gitter.im/intellij-rust/intellij-rust).

## Setting up nightly builds

In addition to preview releases, we also
ship pre-release builds of _intellij-rust_ and _intellij-toml_ in the nightly channel.

To use them you need to follow the
[instructions](https://www.jetbrains.com/idea/help/managing-enterprise-plugin-repositories.html)
of adding additional plugin repository and paste the URL for the one you need:

```yaml
- Rust: https://plugins.jetbrains.com/plugins/nightly/8182
- TOML: https://plugins.jetbrains.com/plugins/nightly/8195
```

Nightly builds are daily snapshots of current development branch. So, it's natural that there may be even
more bugs than in alpha channel. If you find one, we would very appreciate if you file an
[issue](https://github.com/intellij-rust/intellij-rust/issues) on our bugtracker or ping us on our
[chat](https://gitter.im/intellij-rust/intellij-rust).

## Compatible IDEs

The plugin should be compatible with any Intellij based IDE like IDEA, CLion or PyCharm. Latest plugin is guranteed 
to support the latest released major platform version (`2017.3` at the moment of writing), it may support some previous 
or EAP versions.  See `Help > About` menu for IDE version and `Settings > Plugins` menu for plugin version.
