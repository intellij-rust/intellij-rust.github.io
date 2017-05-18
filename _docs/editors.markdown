---
title: Migrating from other editors
---

{% include doc-shortcut-tip.html %}

{% include h title="Emacs" %}

To bring some of Emacs keybindings to intellij-rust, enable `Emacs` keymap in
the settings. This will also enable Emacs tab and Emacs selection.

A crucial thing missing from the Emacs keymap is <kbd>M-x</kbd>. To enable it, change
`Find Action` binding to <kbd>M-x</kbd> in `File > Settings > Keymap`. If you want more
Emacs editing commands and a more uniform handling of UI panels (<kbd>C-g</kbd>, <kbd>C-x 1</kbd>,
<kbd>C-x 0</kbd>) consider [this plugin](https://plugins.jetbrains.com/plugin/7906), but
be warned that it is still in beta.

{% include h title="Vim" %}

To bring your favorite modal editing to _intellij-rust_, please use the
[IdeaVim plugin](https://github.com/JetBrains/ideavim).
