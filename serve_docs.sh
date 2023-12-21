#!/bin/bash

function serve_docs() {
  jupyter-book build docs/
  cd docs/_build/html
  python -m http.server
}

# Initial build and serve
serve_docs &

# Watch for changes in .md and .ipynb files and trigger rebuild
watchmedo shell-command \
  --patterns="*.md;*.rst;*.ipynb;*.yaml;*.yml;*.py;*.js;*.css" \
  --command="serve_docs" \
  .
