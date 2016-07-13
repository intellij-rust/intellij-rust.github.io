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

## Are you going to use `racer` or `RLS`?

No, we plan to implement most of the language analysis from scratch. This is
a lot of work, but the benefits are substantial. We would be able to leverage
IntelliJ Platform infrastructure for incremental analysis and indexing. With
our own analysis we can provide more flexible quick fixes, intentions and typing
assistance.

The same applies to the formatter (that is also from scratch, but we plan to
support running `rustfmt` as an action). It is necessary for proper working
of almost any feature which is modifying source code.
