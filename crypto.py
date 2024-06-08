from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.hmac import hashes, HMAC
import os
import quantumrandom

def create_hmac(data, key):
    h = HMAC(key, hashes.SHA256())
    h.update(data)
    return h.finalize()

def verify_hmac(data, key, tag):
    h = HMAC(key, hashes.SHA256())
    h.update(data)
    h.verify(tag)

"""
This encryption scheme uses Fernet, a 128-bit AES scheme in CBC mode.
"""
def symmetric_encrpytion():

    key = Fernet.generate_key()
    f = Fernet(key)

    token = f.encrypt(b"Here is my secret code!")

    dec = f.decrypt(token)

    print(dec)


"""
This is an HMAC scheme using a []-bit key and SHA-256 hash.
"""
def symmetric_mac():
    # key = Fernet.generate_key()
    # f = Fernet(key)
    # token = f.encrypt(b"Here is my secret code!")

    token = b"hello world!"
    random_key = os.urandom(32)
    tag = create_hmac(token, random_key)
    verify_hmac(token,random_key, tag)


def main():
    symmetric_encrpytion()
    symmetric_mac()

if __name__ == '__main__':
    main()