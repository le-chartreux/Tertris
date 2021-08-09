#!/bin/sh
PATH_TO_DOT="$(dirname "$(readlink -f "$0")")"

python3 -m unittest discover "$PATH_TO_DOT/src" -v