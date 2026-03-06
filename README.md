# 🛡️ BPAS 2.0
### Behavioral Password Attack Simulator (Offline)

**BPAS** is a high-performance, multi-threaded dictionary cracker designed to demonstrate the risks of predictable human password choices. Built with a focus on speed and ease of use, it operates 100% offline to ensure data privacy.

![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg) 
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)

---

## 🚀 Features
* **Multi-Threaded Engine**: Powered by `ThreadPoolExecutor` for Hydra-like cracking speeds.
* **Smart Argument Detection**: Detects wordlist paths directly from the terminal to skip redundant prompts.
* **Professional UI**: Features a vibrant, multi-color ASCII banner and a real-time, single-line status update.
* **Integrated Hash Utility**: Built-in tool for re-encoding plaintext into MD5, SHA1, or SHA256.
* **Privacy-First**: No network connection required; your hashes never leave your machine.

## 🛠️ Installation

```bash
# Clone the repository
git clone [https://github.com/yourusername/BPAS.git](https://github.com/yourusername/BPAS.git)
cd BPAS

# Run the automated installer
chmod +x install.sh
./install.sh
#!/bin/bash

# --- Color Definitions ---
CYAN='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}  BPAS: Behavioral Password Attack Simulator      ${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}[*] Starting automated installation...${NC}"

# 1. Check for Python3
if ! command -v python3 &> /dev/null
then
    echo -e "${RED}[!] Error: Python3 is not installed. Please install it first.${NC}"
    exit 1
fi

# 2. Check for Pip
if ! command -v pip3 &> /dev/null
then
    echo -e "${YELLOW}[!] Pip3 not found. Attempting to install...${NC}"
    sudo apt update && sudo apt install -y python3-pip
fi

# 3. Install Dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
    echo -e "${GREEN}[*] Installing dependencies from requirements.txt...${NC}"
    pip3 install -r requirements.txt --break-system-packages 2>/dev/null || pip3 install -r requirements.txt
else
    echo -e "${YELLOW}[!] requirements.txt not found. Installing colorama manually...${NC}"
    pip3 install colorama
fi

# 4. Set Executive Permissions
if [ -f "bpas.py" ]; then
    chmod +x bpas.py
    echo -e "${GREEN}[*] Permissions set for bpas.py${NC}"
else
    echo -e "${RED}[!] Warning: bpas.py not found in this directory.${NC}"
fi

echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}[SUCCESS] BPAS Installation Complete!${NC}"
echo -e "${YELLOW}To launch the tool, use:${NC}"
echo -e "python3 bpas.py"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
