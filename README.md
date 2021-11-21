# intellij-rust.github.io

## Local development

Install [Ruby](https://www.ruby-lang.org) and [Bundler](http://bundler.io/).
There is `.ruby-version` file for [rbenv](https://github.com/rbenv/rbenv) if you like.
You will probably need GCC, Make, AutoConf and NodeJS installed.  

```bash
$ bundle install
$ bundle exec jekyll serve --future
```

### Windows

If you are using Windows, it's better not to fight with Ruby Installer. I use WSL and works
pretty flawlessly, except file change watching (see
[tracking issue](https://github.com/Microsoft/BashOnWindows/issues/216)). So you'll have to run 
this instead:

```bash
$ bundle exec jekyll serve --no-watch
```

To workaround lack of watching, you can do:

```bash
$ bundle exec jekyll serve --detach
$ while (bundle exec jekyll build --incremental); do sleep 5; done
```
