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
 ### Clone the repository
git clone [https://github.com/yourusername/BPAS.git](https://github.com/yourusername/BPAS.git)
cd BPAS

### Run the automated installer
chmod +x install.sh
./install.sh
