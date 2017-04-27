#!/bin/bash
sudo apt-get update
sudo apt-get -y install build-essential zlib1g-dev liblzma-dev python-magic
wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/firmware-mod-kit/fmk_099.tar.gz
tar fzx fmk_099.tar.gz
