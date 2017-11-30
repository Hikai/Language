#!/bin/bash
git clone https://github.com/cinquemb/firmware-mod-kit-osx
cd ./firmware-mod-kit-osx/src

./configure
make all

brew install coreutils
brew install binwalk
