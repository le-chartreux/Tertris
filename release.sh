#!/bin/bash
# This file cleans all files that are useless for a final user: testing, debug, temporary files...

PATH_TO_DOT="$(dirname "$(readlink -f "$0")")"

read -rp "Make this Tertris folder a release? (y/N) " release
if [ "$release" == "Y" ] || [ "$release" == "y" ]
  then
    echo "Releasing..."
    rm -rf "$PATH_TO_DOT/.git"
    rm -rf "$PATH_TO_DOT/src/debug"
    rm -rf "$PATH_TO_DOT/src/test"
    rm -rf "$PATH_TO_DOT/**/__pycache__"
    rm -f "$PATH_TO_DOT/output.txt"
    rm -f "$PATH_TO_DOT/test.sh"
    rm -f "$PATH_TO_DOT/release.sh"
    echo "Releasing finished."
  else
    echo "Releasing canceled."
fi