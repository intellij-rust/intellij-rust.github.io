---
title: Features
order: 15
---

{% include doc-shortcut-tip.html %}

{% include h title="Navigation" %}

There are a number of actions for efficient navigation across your project and dependencies.

* **Goto Declaration** <kbd>Ctrl+B</kbd> goes to the definition of the symbol at caret.

* **Quick Documentation** <kbd>Ctrl+Q</kbd> shows docs for the symbol at caret.

* **Goto Class** <kbd>Ctrl+N</kbd> search for a struct or enum by name.

* **Goto Symbol** <kbd>Ctrl+Shift+Alt+N</kbd> searches for any symbol (types, methods,
  functions, fields) by name. Together with <kbd>Ctrl+N</kbd> it is the main
  method to explore large projects.

* **File Structure** <kbd>Ctrl+F12</kbd>, <kbd>Alt+7</kbd> brings up an overview of the current file.

* **Goto Super** <kbd>Ctru+U</kbd> navigates to the parent module.


{% include h title="Code Formatter" %}

**Reformat Code** <kbd>Ctrl+Alt+l</kbd> reformats current file or selection using our custom,
fully functional formatter based on IntelliJ's formatting engine, though rustfmt
support is a work in progress. You can use a `Run Configuration` to invoke
`rustfmt`.


{% include h title="Run Configurations" %}

Built-in `Cargo Command` run configuration, automatically created with
<kbd>Ctrl+Shift+F10</kbd> in following contexts:

  * In the file with a `main` function to execute the corresponding binary
    target with `cargo run`.

  * Inside a `#[test]` function to execute a single test.

  * Inside a module to run all containing tests.


{% include h title="Live templates" %}

There is a number of built in live templates and you can define your own.
Different live templates are available in different contexts. Use
<kbd>Ctrl+J</kbd> to list templates available in context.

  * <kbd>p</kbd>, <kbd>pd</kbd>, <kbd>ppd</kbd> - `println!` value with `{}`,
    debug `{:?}` and pretty debug `{:#?}` formats.

  * <kbd>a</kbd>, <kbd>ae</kbd> - `assert!` / `assert_eq!`

  * <kbd>tfn</kbd> - test function boilerplate

  * <kbd>tmod</kbd> - test module boilerplate

  * <kbd>f</kbd>, <kbd>pf</kbd> - \[`pub`\] field name and type, applicable
    inside struct definitions.

  * <kbd>loop</kbd>, <kbd>wihled</kbd>, <kbd>for</kbd> templates. You can select
    a fragment of code and press <kbd>Cltr+Alt+J</kbd> to invoke **Surround With
    Live Template** action.


{% include h title="Intentions" %}

Intentions and quick fixes are micro refactorings automatically available
depending on context. If some intentions are available, a light bulb icon
appears in the editor. You can use <kbd>Alt+Enter</kbd> to invoke a quick fix.

  * **Expand module**: invoke this action inside `foo.rs` file to get `foo/mod.rs`.
    Available as a quick fix for unresolved module declaration.

  * **Contract module**: the opposite of Expand Module.

  * **Create module file**: if you have `mod foo;`, but no `foo.rs` this quick fix
    will create the missing file.

  * **Extract inline module**: move `mod foo { ... }` to a separate file.

  * **Add derive clause**: adds `#[derive(..)]` attribute to structs and enums.

  * **Remove/Add curly braces**: toggles between `use foo::{bar}` and `use foo::bar`.

**Expand module** and **Contract module** are preferred ways to create a new
Rust file. For example if I am in `foo.rs` and I want to create a new child
module `bar.rs`, I type `mod foo;`, press <kbd>Alt+Enter</kbd> to create
`foo/mod.rs` and then press <kbd>Alt+Enter</kbd> again to get an empty
`foo/bar.rs`.
