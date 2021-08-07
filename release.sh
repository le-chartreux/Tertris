#!/bin/bash
# This file cleans all files that are useless for a final user: testing, debug, temporary files...

read -rp "Make this Tertris folder a release? (y/N) " release
if [ "$release" == "Y" ] || [ "$release" == "y" ]
  then
    echo "Releasing..."
    rm -rf "./.git"
    rm -rf "./src/debug"
    rm -rf "./src/test"
    rm -rf "./**/__pycache__"
    rm -rf "./release.sh"
    echo "Releasing finished."
  else
    echo "Releasing canceled."
fi