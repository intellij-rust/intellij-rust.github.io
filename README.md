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

## Docker

Run `intellij-rust.github.io` configuration directly from IntelliJ IDEA. The website will be accessible at `http://localhost:8080/`.
Any changes made in `_posts`, `assets`, `_docs`, and `_includes` directories will be reflected immediately.

Alternatively, you can use the following commands from the terminal:
```bash
$ docker build -t intellij-rust.github.io .
$ docker run \
  -v $PWD/_posts:/intellij-rust.github.io/_posts \
  -v $PWD/assets:/intellij-rust.github.io/assets \
  -v $PWD/_docs:/intellij-rust.github.io/_docs \
  -v $PWD/_includes:/intellij-rust.github.io/_includes \
  -v $PWD/_site:/intellij-rust.github.io/_site \
  -p 8080:8080 -it intellij-rust.github.io
```
