#!/bin/bash

quit_app(){
  echo "Starting canceled."
  exit 1
}

# checking that Python 3 is available
if ! python3 --version > /dev/null 2>&1
then
  echo "Error: Python 3 not installed (unavailable with the python3 command)."
  read -rp "Install Python 3? (Y/n) " install_py
  if [ "$install_py" != "N" ] && [ "$install_py" != "n" ]
  then
    echo -n "Python3 installation..."
    if type apt > /dev/null 2>&1
      then
        echo "with apt"
        sudo apt-get install python3
      elif type yum > /dev/null 2>&1
      then
        echo "with yum"
        sudo yum install python3
      elif type pacman > /dev/null 2>&1
      then
        echo "with pacman"
        sudo pacman -Sy python3
      else
        echo "failure: no supported package manager detected. Try by yourself."
        echo "Python 3 not installed."
        quit_app
      fi;
  else
    echo "This app needs Python 3."
    quit_app
  fi;
fi;


# starting the app
python3 "$(dirname "$(readlink -f "$0")")/src/main.py"
