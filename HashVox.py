#!/usr/bin/env python3
import argparse
import hashlib
import sys
import re

def detect_hash_type(h):
    h = h.strip().lower()

    # Very basic pattern/length-based detection.
    # Add more cases here as needed.
    if re.fullmatch(r"[0-9a-f]{32}", h):
        return "md5"
    elif re.fullmatch(r"[0-9a-f]{40}", h):
        return "sha1"
    elif re.fullmatch(r"[0-9a-f]{64}", h):
        return "sha256"
    elif re.fullmatch(r"[0-9a-f]{128}", h):
        return "sha512"
    else:
        return None

def crack_hash(hash_value, hash_type, wordlist_path):
    hash_value = hash_value.strip().lower()

    try:
        hash_func = getattr(hashlib, hash_type)
    except AttributeError:
        print(f"[!] Hash type {hash_type} not supported by hashlib")
        return None

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for word in f:
                word = word.strip()
                if not word:
                    continue
                candidate_hash = hash_func(word.encode()).hexdigest()
                if candidate_hash == hash_value:
                    return word
    except FileNotFoundError:
        print(f"[!] Wordlist file not found: {wordlist_path}")
        sys.exit(1)

    return None

def main():
    parser = argparse.ArgumentParser(
        description="Detect hash type and crack it using a wordlist"
    )
    parser.add_argument("-H", "--hash", required=True, help="Hash value to crack")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist file")

    args = parser.parse_args()

    hash_value = args.hash
    wordlist = args.wordlist

    # 1) Detect hash type
    hash_type = detect_hash_type(hash_value)
    if not hash_type:
        print("[!] Could not reliably detect hash type (add more cases to detect_hash_type())")
        sys.exit(1)

    print(f"[*] Detected hash type: {hash_type}")

    # 2) Different cases for each hash type
    #    (here logic is same: dictionary attack via hashlib, but you can branch per type)
    if hash_type == "md5":
        print("[*] Using MD5 cracking routine (dictionary attack)")
    elif hash_type == "sha1":
        print("[*] Using SHA1 cracking routine (dictionary attack)")
    elif hash_type == "sha256":
        print("[*] Using SHA256 cracking routine (dictionary attack)")
    elif hash_type == "sha512":
        print("[*] Using SHA512 cracking routine (dictionary attack)")
    else:
        print(f"[!] No cracking routine implemented for {hash_type}")
        sys.exit(1)

    password = crack_hash(hash_value, hash_type, wordlist)

    if password:
        print(f"[+] Hash cracked! Password: {password}")
    else:
        print("[-] Password not found in wordlist")

if __name__ == "__main__":
    main()
