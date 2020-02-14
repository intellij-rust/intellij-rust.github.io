---
title: Quick Start Guide
order: 1
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

In `Settings/Preferences | Languages & Frameworks | Rust`, you can adjust the toolchain settings and select the macro expansion engine<!-- TODO: link the description in Features -->.

![main-settings](/assets/quick-start/qsg_mainsettings.png){:width="750px"}

 If you plan to use an external linter<!-- TODO: link the description in Features --> in addition to the built-in set of code inspections, choose between Cargo Check and Clippy in `Settings/Preferences | Languages & Frameworks | Rust | Cargo`:
 
![external-linter](/assets/quick-start/qsg_linter.png){:width="450px"}


{% include h title="Run Cargo commands" tag="run-commands" %}

To run a Cargo command, click ![Run Cargo Command](/assets/quick-start/cargo@2x.svg){:width="16px"} in the Cargo tool window or press `Ctrl` twice. Type the command in the **Run Anything** popup:

![run-anything](/assets/quick-start/qsg_runanything.png){:width="600px"}


{% include h title="Build" tag="build-prj" %}

- Run `cargo build`
- Press `Ctrl/⌘ + F9`
- Use the `Build` menu


{% include h title="Run" tag="run-prj" %}

- Use the gutter icon next to a program entry point

![run-main](/assets/quick-start/qsg_gutter_main.png){:width="400px"}

- Call `cargo run`
- Double-click an executable target in the Cargo tool window


{% include h title="Test" tag="run-tests" %}

- Use the gutter icon next to a test entry point

![run-tests](/assets/quick-start/qsg_gutter_tests.png){:width="400px"}

- Call `cargo test`
- Double-click a test target in the Cargo tool window

Test runner shows the results in a tree view with indicators of progress, status, and duration of each test:

![test-runner](/assets/quick-start/qsg_testrunner.png){:width="350px"}


{% include h title="Create Cargo Command configurations" tag="run-debug-configs" %}

Every time you run a Cargo command, the IDE creates a temporary run/debug configuration. You can save it and create more configurations of the **Cargo Command** type.

![config-switcher](/assets/quick-start/qsg_configslist.png){:width="200px"}

Go to the `Edit Configurations` dialog, click `+` and select **Cargo Command** from the list of templates.

Name your configuration and provide the command. You can switch Cargo channels (stable, beta, nightly, or dev) separately for each configuration:

![cargo-channel](/assets/quick-start/qsg_cargochannel.png){:width="600px"}

To view stack traces, use the **Backtrace** option, which corresponds to `RUST_BACKTRACE`:

![backtrace](/assets/quick-start/qsg_backtrace.png){:width="600px"}

{% include h title="Run with Code Coverage" tag="coverage" %}
1. Switch to the nightly toolchain in `Settings/Preferences | Languages & Frameworks | Rust`.

2. Run with Code Coverage using one of the options:

    - Select the configuration in the switcher and call **Run with Coverage** from the 
    **Run** menu or press <img src="/assets/quick-start/icons._coverage.png" width="16" alr="coverage icon"/>.
    
    - Use the **Run with Coverage** option from the gutter menu
    ![coverage-gutter](/assets/quick-start/qsg_coverage_gutter.png){:width="400px""}

3. Explore the results in the Coverage tool window and in the editor:
![coverage-results](/assets/quick-start/qsg_coverage_results.png){:width="875px""}

4. For several coverage sessions, you can choose how to view the suites in the `Run | Show Code Coverage Data` dialog.

5. *(Not available for IDEA Community)* To save the results to a file, click 
<img src="/assets/quick-start/icons_coverage_export.png" width="16" alt="coverage results export icon"/> in the Coverage tool window 
or select `Run | Generate Coverage Report` from the main menu.
