#!/bin/sh

# This script removes the need for having docker to build the site locally.
# You can run it through "./dev.sh"

if [ ! -d ".content" ]
then
  echo "No cached '.content' directory found. Fetching the latest data..."
  git clone https://github.com/genicsblog/genicsblog.com .content -q
fi

DIFF_GEM=$(diff -q Gemfile .content/Gemfile)
DIFF_PACKAGE=$(diff -q package.json .content/package.json)

rsync -r --exclude '.content' . .content/
cd .content

if [ ! -d ".bundle" ]; then bundle config set --local path 'vendor'; fi

[ ! -z "$DIFF_GEM" ] && echo "Gemfile change detected!"
[ ! -z "$DIFF_PACKAGE" ] && echo "package.json change detected!"

if [ ! -d "node_modules" ] || [ ! -z "$DIFF_PACKAGE" ]
then
  echo "Installing node dependencies..."
  npm i --silent
fi

if [ ! -d "vendor" ] || [ ! -z "$DIFF_GEM" ]
then
  echo "Installing gem dependencies..."
  bundle install --quiet
fi

bundle exec jekyll serve
