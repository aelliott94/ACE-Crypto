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

    try:
        h.verify(tag)
        print("HMAC verified!")
    except:
        print("HMAC verification failed!")

"""
This encryption scheme uses Fernet, a 128-bit AES scheme in CBC mode.
"""
def symmetric_encrpytion():

    key = Fernet.generate_key()
    f = Fernet(key)

    msg = b"Here is my secret code!"
    print("Message: ", msg)

    token = f.encrypt(msg)
    print("Encrypted: ", token)

    dec = f.decrypt(token)
    print("Decrypted: ", dec)


"""
This is an HMAC scheme using a []-bit key and SHA-256 hash.
"""
def symmetric_mac():
    # key = Fernet.generate_key()
    # f = Fernet(key)
    # token = f.encrypt(b"Here is my secret code!")

    token = b"hello world!"
    print("Token: ", token)
    random_key = os.urandom(256)
    tag = create_hmac(token, random_key)
    print("HMAC: ", tag)
    verify_hmac(token,random_key, tag)


def main():

    print("Starting symmetric encryption algorithm:")
    symmetric_encrpytion()

    print()

    print("Starting symmetric MAC:")
    symmetric_mac()

    print()

    print("Starting asymmetric key exchange:")

    print()

    print("Starting asymmetric signature:")

if __name__ == '__main__':
    main()