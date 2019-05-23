#!/bin/bash

if [ -z "$1" ]
  then
    echo "No argument"
    exit 1
fi

grep -InHr "$1" /path/the/search/ --color=auto
