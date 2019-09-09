---
title: Quick Start Guide
order: 10
---

Apart from minor differences in menu paths and dialogs appearance, instructions below are similar for [IDEA](https://www.jetbrains.com/idea/), [CLion](https://www.jetbrains.com/clion/), and other IntelliJ-based IDEs. Please note that only [Cargo](https://github.com/rust-lang/cargo) projects are supported.

{% include h title="Install IntelliJ Rust" tag="install-plugin" %}

After you have installed Rust using [rustup](https://rustup.rs/) 
or [other installation options](https://github.com/rust-lang/rustup.rs#other-installation-methods), 
go to `Settings / Preferences | Plugins` in your IDE, switch to **Marketplace**, and search for *Rust*:

![install-plugin](/assets/quick-start/qsg_install_plugin.png){:width="750px"}

Click **Install** and restart the IDE.

{% include h title="Create a new project" tag="create-prj" %}

Go to `File | New | Project` (in IDEA) or `File | New Project` (in CLion), and choose **Rust** from the list of project templates in the left-hand pane.

Specify the location, name, and type (application or library) of the project, and set up the toolchain:

![new-project](/assets/quick-start/qsg_new_project.png){:width="750px"}

Click **Create** when ready, and the IDE will generate a project with the following structure:

![new-project-result](/assets/quick-start/qsg_new_project_result.png){:width="750px"}


{% include h title="Open a project" tag="open-prj" %}

Go to `File | Open` and select the folder containing the root `Cargo.toml` file.

Check the Cargo tool window (`View | Tool windows | Cargo`) to make sure your project was imported successfully:

![check-cargo-tw](/assets/quick-start/qsg_cargo_tw.png){:width="350px"}

{% include h title="Clone a repository" tag="open-prj" %}

Go to `VCS | Checkout from Version Control` on the main menu or click **Checkout from Version Control** on the welcome screen:

![qsg_clone](/assets/quick-start/qsg_clone.png){:width="350px"}

In the case of GitHub, provide the repository URL, test the connection using the **Test** button, and click **Clone**:

![qsg_clone_dialog](/assets/quick-start/qsg_clone_dialog.png){:width="750px"}

