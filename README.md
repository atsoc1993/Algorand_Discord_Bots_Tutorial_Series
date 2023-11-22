# Algorand_Discord_Bots_Tutorial_Series
This repository is a guide for discord bot development on Algorand blockchain, meant to be paired with the released youtube series
TERMINAL INSTALLATIONS --- DO NOT USE IN UBUNTU:

## PIP
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

## AIOHTTP --- USE BEFORE INSTALLING DISCORD.PY
```
pip install aiohttp>=3.9.0b0
```

## Discord.py
```
pip install discord.py
```

## Python AlgoSDK
```
pip3 install py-algorand-sdk
```

## UBUNTU TERMINAL INSTALLATIONS --- USE IN UBUNTU:

# Algorand Node Installation
```sudo apt-get update
sudo apt-get install -y gnupg2 curl software-properties-common
curl -o - https://releases.algorand.com/key.pub | sudo tee /etc/apt/trusted.gpg.d/algorand.asc
sudo add-apt-repository "deb [arch=amd64] https://releases.algorand.com/deb/ stable main"
sudo apt-get update
sudo apt-get install -y algorand-devtools
```

# Preparing/Running Algorand Node
```mkdir ~/node
cd ~/node
curl https://raw.githubusercontent.com/algorand/go-algorand/rel/stable/cmd/updater/update.sh -O
chmod 744 update.sh
./update.sh -i -c stable -p ~/node -d ~/node/data -n
goal node start -d data 
goal node catchup GetTheCatchPointFromLinkBelow -d data
```

# Catchpoint Link for Mainnet
https://algorand-catchpoints.s3.us-east-2.amazonaws.com/channel/mainnet/latest.catchpoint

# Algorand Node Commands
'''
goal node start -d data (starts the node)
goal node restart -d data (restarts the node)
goal node stop -d data (stops the node)
goal node catchup GetTheCatchPointFromCatchPoointLink -d data (Catchup the node)
'''

# Basic Terminal Commands
'''
clear ---clears the terminal
mkdir NameOfFolderHere ---creates a folder
ls ---list all folders available in this directory
cd NameOfFolderHere ---enter the folder
cd .. ---Exit directory/Move back out from folder
'''

## LINKS:

# Install Python
https://www.python.org/downloads/
SELECT THE ADD PYTHON TO PATH OPTION!!!

# Install Visual Studio Code
https://code.visualstudio.com/Download

# Microsoft Store Ubuntu LTS
https://www.microsoft.com/store/productId/9MTTCL66CPXJ?ocid=pdpshare

# Algorand Node Documentation
https://developer.algorand.org/docs/run-a-node/setup/install/

# Algorand Node Mainnet Catchpoint:
https://algorand-catchpoints.s3.us-east-2.amazonaws.com/channel/mainnet/latest.catchpoint

# Discord Developer Portal
https://discord.com/developers


