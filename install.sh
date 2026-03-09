#!/bin/bash
# BPAS Dependency Installation Script

echo -e "\e[1;36m[*] BPAS: Starting Automated Installation...\e[0m"

# Update and install pip if missing
sudo apt update && sudo apt install -y python3-pip

# Install required Python libraries
pip3 install -r requirements.txt --break-system-packages

# Set execution permissions for the main tool
chmod +x bpas.py

echo -e "\e[1;32m[+] Installation Complete. Run the tool with: python3 bpas.py\e[0m"
