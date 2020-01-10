---
title: FAQ
order: 3
---

{% include h title="Where is the Rust SDK?" tag="sdk" %}

We don't use the SDK concept to manage Rust versions because it is
specific for IntelliJ IDEA and is not present in other IDEs such as CLion. The path to Cargo is
configured per project in `Settings / Preferences | Languages & Frameworks | Rust`.


{% include h title="What are the compatible IDEs? Is there any difference?" tag="compatible-ides" %}
The plugin works with all IntelliJ-based IDEs of the version 2019.2 and newer. 
Debugger and profiler are currently available in CLion only. See our
[Readme](https://github.com/intellij-rust/intellij-rust#compatible-ides) 
for a complete list of the features that differ depending on the particular IDE.


{% include h title="Does the plugin use RLS, Racer or Rust Analyzer?" tag="racer" %}

No, we implement most of the language analysis from scratch, leveraging 
the IntelliJ Platform infrastructure for incremental analysis and indexing. This approach helps us 
create more flexible quick fixes, intentions, and typing assistance.   

{% include h title="Is there a way to run/debug remotely?" tag="remote" %}

Currently, the only supported solution is remote debug via GDB Server in CLion. For instructions, refer to the 
[article](https://www.jetbrains.com/help/clion/rust-support.html#remote-debug)
in CLion webhelp.

{% include h title="How can I contribute?" tag="contribute" %}
You are welcome to contribute to the plugin sources if you found some issues or miss certain functionality.
Take a look at these two documents: [Contributing](https://github.com/intellij-rust/intellij-rust/blob/master/CONTRIBUTING.md)
and [Architecture](https://github.com/intellij-rust/intellij-rust/blob/master/ARCHITECTURE.md). 
If you are not sure where to start, consider the issues tagged with [help wanted](https://github.com/intellij-rust/intellij-rust/labels/help%20wanted).
