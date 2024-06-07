from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.hmac import hashes, HMAC
import os


key = Fernet.generate_key()
f = Fernet(key)


key2 = Fernet.generate_key()
f2 = Fernet(key2)


token = f.encrypt(b"Here is my secret code!")

# HMAC(random key, hash)
h = HMAC(os.urandom, hashes.SHA256())

h.update(b"message to hash")

h_copy = h.copy() # get a copy of `h' to be reused

h.verify(b"signature")

h_copy.verify(b"an incorrect signature")

print(token)


dec = f.decrypt(token)


print(dec)