---
title: Quick start
order: 10
---

{% include doc-shortcut-tip.html %}

{% include h title="Getting Rust and IntelliJ IDEA" tag="getting-rust" %}

You can use any JetBrains IDE to develop Rust. If you are not sure which one to
choose, download
[IntelliJ IDEA community edition](https://www.jetbrains.com/idea/), it's free. Install the
plugin via `Settings > Plugins > Install JetBrains plugin` menu.

It's most convenient to use [rustup.rs](https://rustup.rs/) to install Rust.
Using your operating system's package manager will work as well, but you will
need to download sources of the standard library manually.

{% include h title="Create new project..." tag="new-project" %}

After you have installed the plugin you can **create new** project.

![idea-new-project](/assets/quick-start/idea-new-project.png){:width="750px"}

Select Rust project type.

![idea-select-project-type](/assets/quick-start/idea-select-project-type.png){:width="750px"}

And specify a project name and location.

![idea-project-location](/assets/quick-start/idea-project-location.png){:width="750px"}

If you are using other IDE ([CLion](https://www.jetbrains.com/clion/), [PyCharm](https://www.jetbrains.com/pycharm/), etc.) 
you will see slightly different interface while creating a new project.

![clion-new-project](/assets/quick-start/clion-new-project.png){:width="750px"}

And then select Rust project type and specify project location.

![clion-project-location](/assets/quick-start/clion-project-location.png){:width="750px"}

{% include h title="...or open existing one" tag="open-idea" %}

You can also **import** existing project from source.

![idea-import](/assets/quick-start/idea-import-project.png){:width="750px"}

Select the directory with the project. The directory must contain a `Cargo.toml`
file.

![select-directory](/assets/quick-start/select-project.png)

Use _from existing sources_ import.

![from-sources](/assets/quick-start/import-from-existing-sources.png)

Check that the directory is recognized as a Rust project:

![rust-source](/assets/quick-start/rust-source.png)

Select a Rust toolchain. It's OK if there is no rustup.

![import-toolchain-step](/assets/quick-start/import-toolchain-setup.png)

To import project in other IDEs just use **open** option.

![clion-import](/assets/quick-start/clion-import-project.png){:width="750px"}

And select project directory.

If you want to check if the project is imported successfully, or to link
additional Cargo projects to an exitising IDE project, you could use Cargo
toolwindow:

![cargo-toolwindow](/assets/quick-start/cargo-toolwindow.png)

{% include h title="After your project is ready..." tag="project-ready" %}

Check that the basic functionality is working. Try **Goto Symbol**
<kbd>Ctrl+Alt+Shift+N</kbd>, **Goto Declaration** <kbd>Ctrl+B</kbd> and
completion <kbd>Ctrl+Space</kbd>.


{% include feature-video.html v="quick-start/features" %}
