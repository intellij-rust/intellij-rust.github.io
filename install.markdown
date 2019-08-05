---
layout: page
title: Install IntelliJ Rust
---

## Stable builds

IntelliJ Rust is in active development, and we regularly publish new stable builds to the JetBrains plugin [repository](https://plugins.jetbrains.com/plugin/8182).
You can download and install them directly from `Settings / Preferences | Plugins | Marketplace` in your IDE.

## Nightly builds

In addition to stable releases, we also ship nightly snapshots of the _intellij-rust_ development branch. 
To use the nightly channel, [add a custom plugin repository](https://www.jetbrains.com/idea/help/managing-enterprise-plugin-repositories.html#repos)
 and set the following URL:

```yaml
https://plugins.jetbrains.com/plugins/nightly/8182
```

## Compatible IDEs

The plugin is compatible with all Intellij-based IDEs like IDEA, CLion, or PyCharm. The latest plugin version supports the latest released platform version (for example, `2019.2`).

## Bug reports and feature requests

Please use our [tracker](https://github.com/intellij-rust/intellij-rust/issues/new). 
You can get there quickly right from the IDE: 
call `Create New Issue` on a selected piece of code, and you'll jump to a pre-filled issue creating form.

Also feel free to ping us on [Gitter](https://gitter.im/intellij-rust/intellij-rust).
