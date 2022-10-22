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


def main():
    os.system("clear")
    print(BANNER)

    key = b"password"
    plaintext = "W0RDL1ST 4TT4CK 1S 3FF1C13NT"
    nonce, ciphertext, tag = utils.encrypt(plaintext, key)

    print("========== How does it work ? ==========")
    print("From a given file containing a list of keys")
    print("Does this key allows to decrypt the ciphertext ? Y/N")

    print()

    print("========== PARAMETERS ==========")
    print(f"Using '{key.decode()}' as key.")
    print(f"Plaintext to find : {plaintext}")
    print(f"Cipher text: {ciphertext}")
    print("Wordlist size : 10000 words")
    print()
    print("===== What do we have ? =====")
    print(f"Cipher text: {ciphertext}")

    print()
    input("Press enter to start...")
    print()

    start = time.time()

    bruteforce_wordlist(ciphertext, tag, nonce, "wordlist.txt")

    end = time.time()

    print("Secret plaintext found in {:.2f} seconds".format(end - start))


if __name__ == "__main__":
    main()
