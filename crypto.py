from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.hmac import hashes, HMAC
import os


def create_hmac(data):
    h = HMAC(key, hashes.SHA256())
    h.update(data)
    return h.finalize()

def verify_hmac(data, tag):
    h = HMAC(key, hashes.SHA256())
    h.update(data)
    h.verify(tag)

key = Fernet.generate_key()
f = Fernet(key)


token = f.encrypt(b"Here is my secret code!")

# # HMAC(random key, hash)
# key = os.urandom(32)
# h = HMAC(key, hashes.SHA256())
tag = create_hmac(token)

print("verifying key 1")

verify_hmac(token,tag)

print("key 1 verified")

print(token)


dec = f.decrypt(token)


print(dec)