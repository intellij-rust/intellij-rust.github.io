---
title: Quick start
order: 10
---

{% include doc-shortcut-tip.html %}

{% include h title="Getting Rust and IntelliJ IDEA" tag="getting-rust" %}

You can use any JetBrains IDE to develop Rust. If you are not sure which one to
choose, download
[IntelliJ IDEA community edition](https://www.jetbrains.com/idea/). Install the
plugin via `Settings > Plugins > Browse repositories` menu.

It's most convenient to use [rustup.rs](https://rustup.rs/) to install Rust.
Using your operating system's package manager will work as well, but you will
need to download sources of the standard library manually.

{% include h title="Opening existing project" tag="open-idea" %}

After you have installed the plugin into IntelliJ IDEA you can **import** a
project from source:

![idea-import](/assets/quick-start/import-project.png)

Select the directory with the project. The directory must contain a `Cargo.toml`
file.

![select-directory](/assets/quick-start/select-project.png)

Use _from existing sources_ import.

![from-sources](/assets/quick-start/import-from-existing-sources.png)

Check that the directory is recognized as a Rust project:

![rust-source](/assets/quick-start/rust-source.png)

Select a Rust toolchain. It's OK if there is no rustup.

![import-toolchain-step](/assets/quick-start/import-toolchain-setup.png)

Wait until Cargo downloads all project dependencies. Open any Rust file. You
should see a suggestion to add the sources of the standard library:

![download-stdlib](/assets/quick-start/download-stdlib-notification.png)


If you are using rustup, just click **Download**. Otherwise, download the
archive with the source code from
[rust-lang.org](https://www.rust-lang.org/en-US/downloads.html), extract it and
click **Attach**.


{% include h title="After your project is ready..." tag="project-ready" %}

Check that the basic functionality is working. Try **Goto Symbol**
<kbd>Ctrl+Alt+Shift+N</kbd>, **Goto Declaration** <kbd>Ctrl+B</kbd> and
completion <kbd>Ctrl+Space</kbd>.


{% include feature-gfy.html n="SadCourteousDobermanpinscher" %}
