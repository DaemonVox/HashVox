# HashVox

HashVox is a simple Python tool that **detects common hash types** and then **attempts to crack them using a wordlist**.

Currently supported (by length/pattern):

- MD5 (32 hex)
- SHA1 (40 hex)
- SHA256 (64 hex)
- SHA512 (128 hex)

Detection is heuristic and meant for practice/learning, not for highly reliable identification.

---

## Features

- Automatic hash type detection based on length and regex.
- Separate cracking routines per hash type (easy to extend).
- Dictionary-based attack using a user-supplied wordlist.
- Minimal dependencies (only Python standard library).

---

## Usage

1. git clone https://github.com/DaemonVox/HashVox.git

2. cd HashVox

3. python3 hashvox.py -H <hash_value> -w <wordlist_path>

If the password is in the wordlist, HashVox will print:

---

## Example

python3 hashvox.py -H 5d41402abc4b2a76b9719d911017c592 -w rockyou.txt
