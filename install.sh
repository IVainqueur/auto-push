# move the main files to a hidden directory in the home folder
# the hidden directory would be called .auto-push

cp ./auto-push ./main.py ./methods.py ~/.auto-push

# Add the directory to PATH

export PATH=$HOME/.auto-push:$PATH

echo "\x1B[32m===================================="
echo "   THANKS FOR INSTALLING AUTO-PUSH  "
echo "====================================\x1B[0m"