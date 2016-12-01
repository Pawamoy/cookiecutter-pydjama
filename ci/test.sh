#!/bin/bash -eE
shopt -s xpg_echo

if [ -z "$1" ]; then
    echo "Usage:"
    echo "   $0 env-name"
    exit 1
fi

echo "\033[1;36m================================\033[0m"
echo "\033[1;36m= Testing: $1\033[0m"
echo "\033[1;36m================================\033[0m"

# Using tox through tox with long env names results in too long shebang issues in pip script.
# See https://github.com/tox-dev/tox/issues/66.
# A workaround here is to use a truncation of a hash of the env name to reduce the size of the
# path and hence the size of the shebang in pip script.
# With the current env names, truncate to 4 characters results in 1 collision.
# Truncate to 6 should be enough for future changes.

# The thing is not everybody can or wants to use /tmp, and sometimes this very code will be
# nested in a very long path, so this trick won't work. The fix should come from tox or
# virtualenv/pip (the one who creates the pip script) themselves.

workdir="/tmp/$(echo $1 | shasum | cut -c-6).tox"
rm -rf "${workdir}/python-nameless"
config_file="ci/envs/${1#*-}.cookiecutterrc"
cookiecutter --no-input --config-file "${config_file}" -o "${workdir}" .
cd "${workdir}/python-nameless"
git init .
git add -A .
git commit -m "initial."
bumpversion patch
bumpversion minor
bumpversion major
sed -i 's/sphinx-build -b linkcheck/#/' tox.ini
tox
