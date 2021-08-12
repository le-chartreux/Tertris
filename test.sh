#!/bin/bash
PATH_TO_DOT="$(dirname "$(readlink -f "$0")")"
CLASSIC_COMMAND="python3 -m unittest discover "$PATH_TO_DOT/src""

if [[ "$@" =~ "-v" ]]
then
  CLASSIC_COMMAND="$CLASSIC_COMMAND -v"
fi

if [[ "$@" =~ "-s" ]]
then
  CLASSIC_COMMAND="SLOW_TESTS=1 $CLASSIC_COMMAND"
fi

eval "$CLASSIC_COMMAND"
