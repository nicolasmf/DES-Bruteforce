from Crypto.Cipher import DES


def encrypt(msg, key):
    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode("ascii"))
    return nonce, ciphertext, tag


def decrypt(nonce, ciphertext, tag, key):
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)

    try:
        cipher.verify(tag)
        return plaintext.decode("ascii")
    except:
        return False
