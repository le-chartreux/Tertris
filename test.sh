#!/bin/sh
PATH_TO_DOT="$(dirname "$(readlink -f "$0")")"

if [ $# = 1 ] && [ "$1" = "-v" ]
then
  python3 -m unittest discover "$PATH_TO_DOT/src" -v
else
  python3 -m unittest discover "$PATH_TO_DOT/src"
fi