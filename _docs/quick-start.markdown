---
title: Quick Start Guide
order: 10
---

Below you can find general instructions on how to install the plugin and work with Rust projects in [IDEA](https://www.jetbrains.com/idea/), [CLion](https://www.jetbrains.com/clion/), and other IntelliJ-based IDEs. Menu paths and dialog appearance may slightly vary depending on a particular IDE.

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

Go to `File | Open` and select the folder containing the root `Cargo.toml` file. Check the Cargo tool window (`View | Tool windows | Cargo`) to make sure your project was imported successfully:

![check-cargo-tw](/assets/quick-start/qsg_cargo_tw.png){:width="300px"}

{% include h title="Clone a repository" tag="clone-repo" %}

Go to `VCS | Checkout from Version Control` on the main menu or click **Checkout from Version Control** on the welcome screen:

![qsg_clone](/assets/quick-start/qsg_clone.png){:width="300px"}

In the case of GitHub, provide the repository URL, test the connection using the **Test** button, and click **Clone**:

![qsg_clone_dialog](/assets/quick-start/qsg_clone_dialog.png){:width="700px"}

{% include h title="Configure project settings" tag="settings" %}

In `Settings/Preferences | Languages & Frameworks | Rust`, you can adjust the toolchain settings and select the macro expansion engine.

![main-settings](/assets/quick-start/qsg_mainsettings.png){:width="750px"}

 If you plan to use an external linter, select it in `Settings/Preferences | Languages & Frameworks | Rust | Cargo`:
 
 ![external-linter](/assets/quick-start/qsg_linter.png){:width="450px"}


{% include h title="Run Cargo commands" tag="run-commands" %}

To run a Cargo command, click ![Run Cargo Command](/assets/quick-start/cargo@2x.svg){:width="16px"} in the Cargo tool window or press `Ctrl` twice. Type the command in the **Run Anything** popup:

![run-anything](/assets/quick-start/qsg_runanything.png){:width="600px"}

Every time you run a Cargo command, the IDE creates a temporary run/debug configuration. You can save it and create more configurations of the **Cargo Command** type in `Edit Configurations`.

![config-switcher](/assets/quick-start/qsg_configslist.png){:width="200px"}

You can switch Cargo channels (stable, beta, nightly, or dev) separately for each configuration:

![cargo-channel](/assets/quick-start/qsg_cargochannel.png){:width="600px"}

{% include h title="Build" tag="build-prj" %}

To build a project, do one of the following:
- Run `cargo build`
- Press `Ctrl/⌘ + F9`
- Use actions from the `Build` menu
- Run any **Cargo Command** configuration (by default, it includes a build step)

{% include h title="Run" tag="run-prj" %}
To run an application, choose from these options:
- Call `cargo run` (if the executable is ready)
- Create and run a **Cargo Command** configuration with `run` in the **Command** field (build will be performed automatically).

To view stack traces, use the **Backtrace** option in the configuration settings:

![backtrace](/assets/quick-start/qsg_backtrace.png){:width="600px"}

{% include h title="Test" tag="run-tests" %}

When you run `cargo test`, the tests are shown in a tree view with the indicators of progress, status, and duration for each of them. 

You can rerun the test manually or toggle automatic rerun on changes in your code.

![test-runner](/assets/quick-start/qsg_testrunner.png){:width="350px"}
