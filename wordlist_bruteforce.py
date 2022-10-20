import os
import string
import sys
import time
import utils

BANNER = """
 __      __          _ _ _    _     __  __     _   _            _ 
 \ \    / /__ _ _ __| | (_)__| |_  |  \/  |___| |_| |_  ___  __| |
  \ \/\/ / _ \ '_/ _` | | (_-<  _| | |\/| / -_)  _| ' \/ _ \/ _` |
   \_/\_/\___/_| \__,_|_|_/__/\__| |_|  |_\___|\__|_||_\___/\__,_|
"""


def bruteforce_wordlist(ciphertext, tag, nonce, wordlist) -> None:
    with open(wordlist) as f:
        i = 0
        percent = 0
        wordlist_length = 10000
        for key in f:
            try:
                i += 1
                percent = i / wordlist_length * 100
                key = key.strip()
                plaintext = utils.decrypt(nonce, ciphertext, tag, key.encode("utf-8"))
                print(
                    "Trying key: {}, Advancement : {:.2f}%".format(key, percent),
                    end="\r",
                )
                sys.stdout.write("\033[K")
                if plaintext:
                    print(f"Plaintext '{plaintext}' found with key : {key}")
            except ValueError:
                pass


def countdown():
    for i in range(10, 0, -1):
        print(f"Starting in {i}...", end="\r")
        sys.stdout.write("\033[K")
        time.sleep(1)


def main():
    os.system("clear")
    print(BANNER)

    key = b"password"
    plaintext = "Hello World"
    nonce, ciphertext, tag = utils.encrypt(plaintext, key)

    print("========== PARAMETERS ==========")
    print(f"Using '{key.decode()}' as key.")
    print(f"Plaintext to find : {plaintext}")
    print(f"Cipher text: {ciphertext}")
    print("Wordlist size : 10000 words")
    print()
    countdown()
    print()

    start = time.time()

    bruteforce_wordlist(ciphertext, tag, nonce, "wordlist.txt")

    end = time.time()

    print("Secret plaintext found in {:.2f} seconds".format(end - start))


if __name__ == "__main__":
    main()
