#!/usr/bin/env python3
"""
Behavioral Password Attack Simulator (Offline)
Author: Your Name
Purpose: Analyze password attack behavior using offline hash comparison
"""

import hashlib
import time
import argparse
import os
import sys
import getpass


# ---------------- Banner ----------------
def display_banner(author_name="Your Name"):
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

    banner = f"""
{MAGENTA}{BOLD}    ____  ____   _    ____  
   | __ )|  _ \\ / \\  / ___| 
   |  _ \\| |_) / _ \\ \\___ \\ 
   | |_) |  __/ ___ \\ ___) |
   |____/|_| /_/   \\_\\____/ {END}
   
{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{END}
{BOLD}  Behavioral Password Attack Simulator ({RED}OFFLINE{END}{BOLD}){END}
{BLUE}  Developed by: {YELLOW}{author_name}{END}
{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{END}
"""
    print(banner)


# ---------------- Hashing ----------------
def hash_password(password, algorithm="sha256"):
    if algorithm == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(password.encode()).hexdigest()
    else:
        raise ValueError("Unsupported hash algorithm")


# ---------------- Hash Re-Encode Utility ----------------
def hash_reencode():
    print("\n[ HASH RE-ENCODING MODE ]")

    password = getpass.getpass("[?] Enter plaintext password: ")

    algorithm = input(
        "[?] Convert to which hash (md5 / sha1 / sha256): "
    ).strip().lower()

    if algorithm not in ["md5", "sha1", "sha256"]:
        print("[!] Unsupported hash algorithm")
        return

    new_hash = hash_password(password, algorithm)

    print("\n[✔] Hash Generated Successfully")
    print(f"    Algorithm : {algorithm}")
    print(f"    Hash      : {new_hash}")


# ---------------- Attack Strategies ----------------
def dictionary_attack(target_hash, wordlist, algorithm):
    attempts = 0
    start = time.time()

    for word in wordlist:
        attempts += 1
        if hash_password(word, algorithm) == target_hash:
            return True, word, attempts, time.time() - start

    return False, None, attempts, time.time() - start


def hybrid_attack(target_hash, wordlist, algorithm):
    attempts = 0
    start = time.time()

    for word in wordlist:
        for suffix in ["1", "12", "123", "2023", "2024", "!"]:
            attempts += 1
            candidate = word + suffix
            if hash_password(candidate, algorithm) == target_hash:
                return True, candidate, attempts, time.time() - start

    return False, None, attempts, time.time() - start


def rule_based_attack(target_hash, wordlist, algorithm):
    attempts = 0
    start = time.time()

    rules = [
        lambda w: w.capitalize(),
        lambda w: w.upper(),
        lambda w: w.replace("a", "@").replace("o", "0"),
        lambda w: w + "123",
        lambda w: w + "!"
    ]

    for word in wordlist:
        for rule in rules:
            attempts += 1
            candidate = rule(word)
            if hash_password(candidate, algorithm) == target_hash:
                return True, candidate, attempts, time.time() - start

    return False, None, attempts, time.time() - start


# ---------------- Simulation Controller ----------------
def run_simulation(target_hash, wordlist_path, algorithm):
    try:
        with open(wordlist_path, "r", errors="ignore") as f:
            wordlist = [w.strip() for w in f if w.strip()]
    except FileNotFoundError:
        print("[!] Wordlist file not found")
        sys.exit(1)

    print("\n[+] Running Dictionary Attack")
    print_result("Dictionary", dictionary_attack(target_hash, wordlist, algorithm))

    print("\n[+] Running Hybrid Attack")
    print_result("Hybrid", hybrid_attack(target_hash, wordlist, algorithm))

    print("\n[+] Running Rule-Based Attack")
    print_result("Rule-Based", rule_based_attack(target_hash, wordlist, algorithm))


def print_result(strategy, result):
    success, password, attempts, duration = result

    if success:
        print(f"[✔] {strategy} SUCCESS")
        print(f"    Password Found : {password}")
    else:
        print(f"[✘] {strategy} FAILED")

    print(f"    Attempts       : {attempts}")
    print(f"    Time Taken     : {duration:.2f} seconds")


# ---------------- CLI ----------------
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner(author_name="___ZORO___")

    print("[1] Run Password Attack Simulation")
    print("[2] Hash Re-Encode Utility")

    choice = input("\n[?] Select option: ").strip()

    if choice == "2":
        hash_reencode()
        sys.exit(0)

    parser = argparse.ArgumentParser(
        description="Offline Behavioral Password Attack Simulator"
    )
    parser.add_argument(
        "wordlist",
        nargs="?",
        help="Path to wordlist (optional)"
    )

    args = parser.parse_args()

    wordlist_path = args.wordlist or input("[?] Enter wordlist path: ").strip()
    target_hash = input("[?] Enter target hash: ").strip()

    algorithm = input(
        "[?] Choose hash algorithm (md5 / sha1 / sha256) [sha256]: "
    ).strip().lower()

    if not algorithm:
        algorithm = "sha256"

    if algorithm not in ["md5", "sha1", "sha256"]:
        print("[!] Unsupported hash algorithm")
        sys.exit(1)

    run_simulation(target_hash, wordlist_path, algorithm)
