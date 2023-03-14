FROM ruby:3.2

RUN apt-get update && apt-get install -y build-essential

COPY . /intellij-rust.github.io
WORKDIR /intellij-rust.github.io

RUN gem install github-pages jekyll jekyll-feed && bundle add webrick && bundle update && bundle install

EXPOSE 8080

WORKDIR /intellij-rust.github.io
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--port", "8080", "--future"]
