---
title: Setting up nightly builds
---
In addition to [stable](https://plugins.jetbrains.com/plugin/8182) releases, we also
ship pre-release builds of _intellij-rust_ and _intellij-toml_ in the nightly channel.

To use them you need to follow the
[instructions](https://www.jetbrains.com/idea/help/managing-enterprise-plugin-repositories.html)
of adding additional plugin repository and paste the URL for the one you need:

```yaml
- Rust: https://plugins.jetbrains.com/plugins/nightly/8182
- TOML: https://plugins.jetbrains.com/plugins/nightly/8195
```

As this is a preview release, something might go wrong. So, be brave to face some nasty bugs.
If you find one, we would very appreciate if you file an [issue](https://github.com/intellij-rust/intellij-rust/issues)
on our bugtracker or ping us on our [chat](https://gitter.im/intellij-rust/intellij-rust).
