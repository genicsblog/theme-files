#!/bin/sh

# This script removes the need for having docker to build the site locally.
# You can run it through "./dev.sh"

# move out of the .content folder once script is closed
function cleanup () {
  cd ..
}

trap "cleanup" 2

if [ ! -d ".content" ]
then
  echo "No cached '.content' directory found. Fetching the latest data..."
  git clone https://github.com/genicsblog/genicsblog.com .content -q
fi

rsync -r --exclude '.content' . .content/
cd .content

if [ ! -d "node_modules" ]
then
  echo "Installing node dependencies..."
  npm i --silent
fi

if [ ! -d "vendor" ]
then
  echo "Installing gem dependencies..."
  bundle config set --local path 'vendor'
  bundle install --quiet
fi

bundle exec jekyll serve
