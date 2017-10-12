---
title: Quick start
order: 10
---

{% include doc-shortcut-tip.html %}

{% include h title="Getting Rust and IntelliJ IDEA" tag="getting-rust" %}

You can use any JetBrains IDE to develop Rust. If you are not sure which one to
choose, download
[IntelliJ IDEA community edition](https://www.jetbrains.com/idea/). Install the
plugin via `Settings > Plugins > Install JetBrains plugin` menu.

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

If you want to check if the project is imported successfully, or to link
additional Cargo projects to an exitising IDE project, you could use Cargo
toolwindow:

![cargo-toolwindow](/assets/quick-start/cargo-toolwindow.png)

{% include h title="After your project is ready..." tag="project-ready" %}

Check that the basic functionality is working. Try **Goto Symbol**
<kbd>Ctrl+Alt+Shift+N</kbd>, **Goto Declaration** <kbd>Ctrl+B</kbd> and
completion <kbd>Ctrl+Space</kbd>.


{% include feature-video.html v="quick-start/features" %}
