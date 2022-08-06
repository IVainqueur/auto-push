#!/bin/sh

# move the main files to a hidden directory in the home folder
# the hidden directory would be called .auto-push

mkdir -p ~/.auto-push && cp ./auto-push ./main.py ./methods.py ~/.auto-push

# Add the directory to PATH

export PATH=$HOME/.auto-push:$PATH

GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo "${GREEN}===================================="
echo "   THANKS FOR INSTALLING AUTO-PUSH  "
echo "====================================${NC}"