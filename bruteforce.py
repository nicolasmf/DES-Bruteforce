import itertools
import os
import string
import sys
import time
import utils

CHARS = string.ascii_lowercase

BANNER = """
  ___          _        __                  __  __     _   _            _ 
 | _ )_ _ _  _| |_ ___ / _|___ _ _ __ ___  |  \/  |___| |_| |_  ___  __| |
 | _ \ '_| || |  _/ -_)  _/ _ \ '_/ _/ -_) | |\/| / -_)  _| ' \/ _ \/ _` |
 |___/_|  \_,_|\__\___|_| \___/_| \__\___| |_|  |_\___|\__|_||_\___/\__,_|
"""


def bruteforce(ciphertext, tag, nonce) -> str:

    i = 0
    percent = 0
    lenght = 110075314176

    for key in itertools.product(CHARS, repeat=8):
        i += 1
        percent = i / lenght * 100
        key = "".join(key)
        plaintext = utils.decrypt(nonce, ciphertext, tag, key.encode("ascii"))

        print(
            "Trying key: {} Advancement : {:.5f}%".format("".join(key), percent),
            end="\r",
        )
        sys.stdout.write("\033[K")

        if plaintext:
            print(f"Plaintext '{plaintext}' found with key : {key}")
            return


def countdown():
    for i in range(3, 0, -1):
        print(f"Starting in {i}...", end="\r")
        sys.stdout.write("\033[K")
        time.sleep(1)


def main():
    os.system("clear")
    print(BANNER)

    key = b"aaaavnrd"
    plaintext = "Hello World"
    nonce, ciphertext, tag = utils.encrypt(plaintext, key)

    print("========== PARAMETERS ==========")
    print(f"Using '{key.decode()}' as key.")
    print(f"Plaintext to find : {plaintext}")
    print(f"Cipher text: {ciphertext}")
    countdown()
    print()

    start = time.time()

    bruteforce(ciphertext, tag, nonce)

    end = time.time()
    print("Secret plaintext found in {:.2f} seconds".format(end - start))


if __name__ == "__main__":
    main()
