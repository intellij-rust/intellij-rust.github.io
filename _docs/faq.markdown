---
title: FAQ
order: 999999
---

## What's the progress on code completion?

A decent amount of completion intelligence is
already implemented, but there is definitely a lot more to do. Here are some
examples of what works and what does not work (as of **June 20**).

```rust
use std::collections::HashMap;
                        //^ completes to HashMap or HashSet

struct S {
    mapping: HashMap<i32, i32>
            //^ knows that HashMap is in scope, so completes
}

fn main() {
    let mut thing = S { mapping: HashMap::default() };
                                          //^ no completion here yet :(

    //v completes `thing`
    thing.mapping.insert(92, 92);
          //^ completes `mapping`
                  //^ but does not know about `insert` yet :(
}
```

Remember, if the smart completion does not work for your particular case,
you can always invoke "dumb completion" via <kbd>Alt+/</kbd>. It merely suggests
identifiers already present in the file, but works surprisingly well.

## Why do you not use `racer` for completion?

There are multiple reasons for this decision.

First of all, `racer`'s interface is incomplete and designed to work with
physical files, while IntelliJ Platform heavily uses in-memory buffers and
virtual file systems. For example, we fetch standard library sources for
analysis from a zip of the `rustc` sources.

Also, `racer` provides only code completion and basic navigation, while for
other features, like intentions, quick fixes, quick doc etc., we have anyway
to implement custom code analysis.

The same applies to the formatter (that is also hand written, but we plan to
support running `rustfmt` as an action), which is necessary for proper working
of almost any feature which is modifying source code.
