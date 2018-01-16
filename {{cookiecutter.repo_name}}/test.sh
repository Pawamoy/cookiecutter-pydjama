#!/usr/bin/env bash

set -e

if ! command -v pyenv &>/dev/null; then
  echo "Please install pyenv: https://github.com/pyenv/pyenv" >&2
  exit 1
fi

PYTHON_VERSIONS=""
DEPENDENCIES=""

while [ $# -ne 0 ]; do
  case $1 in
    -p|--python)
      if ! PYTHON_VERSIONS=$(pyenv versions --bare | grep "$2"); then
        echo "Python version(s) $2 are not installed" >&2
        echo "Trying to install with pyenv:"
        pyenv install "$2" || exit 1
        PYTHON_VERSIONS="$2"
      fi
      shift
    ;;
    -d|--dependencies) DEPENDENCIES="${2+x}" ;;
  esac
  shift
