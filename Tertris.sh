#!/bin/sh

python3 "$(dirname "$(readlink -f "$0")")/src/main.py"
