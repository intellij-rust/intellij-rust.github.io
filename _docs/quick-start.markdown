---
title: Quick start
order: 10
---

{% include doc-shortcut-tip.html %}

{% include h title="Opening existing project" tag="open-idea" %}

After you have installed the plugin into IntelliJ IDEA you can **import** a
project from source:

![idea-import](/assets/quick-start/import-project.png)

Select the directory with the project.

![select-directory](/assets/quick-start/select-project.png)

Use _from existing sources_ import.

![from-sources](/assets/quick-start/import-from-existing-sources.png)

Click through the wizard steps and select a Rust toolchain:

![import-toolchain-step](/assets/quick-start/import-toolchain-setup.png)

Wait until Cargo downloads all project dependencies. Open any Rust file. You
should see a suggestion to download the standard library:

![download-stdlib](/assets/quick-start/download-stdlib-notification.png)


Select a directory to download the library to.

![download-stdlib-dir](/assets/quick-start/download-stdlib-directory.png)


Wait until the library is downloaded and indexed.


{% include h title="After your project is ready..." tag="project-ready" %}

Check that the basic functionality is working. Try **Goto Symbol**
<kbd>Ctrl+Alt+Shift+N</kbd>, **Goto Declaration** <kbd>Ctrl+B</kbd> and
completion <kbd>Ctrl+Space</kbd>.


{% include feature-gfy.html n="SadCourteousDobermanpinscher" %}
