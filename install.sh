#!/bin/sh

# move the main files to a hidden directory in the home folder
# the hidden directory would be called .auto-push

mkdir -p ~/.auto-push && cp ./auto-push ./main.py ./methods.py ~/.auto-push

# Add the directory to PATH

export PATH=$PATH:$HOME/.auto-push

echo "export PATH=\$PATH:$HOME/.auto-push;" >> ~/.bashrc
source ~/.bashrc

GREEN='\033[0;32m'
NC='\033[0m' # No Color/ Clear all formatting

echo "${GREEN}===================================="
echo "   THANKS FOR INSTALLING AUTO-PUSH  "
echo "====================================${NC}"