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
## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOURUSERNAME/bpas.git && cd bpas
```

### 2. Run the Installer

```bash
chmod +x install.sh && ./install.sh
```

### 3. Run BPAS

```bash
python3 bpas.py
```

---

## Usage

Run the simulator:

```bash
python3 bpas.py
```

Select one of the options:

1. Run Password Attack Simulation  
2. Hash Re-Encode Utility

---

## Features

- Offline dictionary password attack simulation
- Supports **MD5, SHA1, SHA256**
- Real-time password cracking attempt display
- Hash re-encoding utility
- Educational cybersecurity tool
