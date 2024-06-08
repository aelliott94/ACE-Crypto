# importing libraries
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.hmac import hashes, HMAC
import os

from datetime import datetime, timedelta

def create_hmac(data, key):
    h = HMAC(key, hashes.SHA256())
    h.update(data)
    return h.finalize()

def verify_hmac(data, key, tag):
    h = HMAC(key, hashes.SHA256())
    h.update(data)
    h.verify(tag)

def vertifyTimestamp(data):
    date_format = "%Y-%m-%d %H:%M:%S.%f"

    data = data.decode("utf-8").split(" ~ ")[1]

    date_data = datetime.strptime(data, date_format)
    
    return(abs(datetime.now() - date_data) < timedelta(seconds=1))

# generating Symettric private key to share

symettric_key = Fernet.generate_key()

print(symettric_key)
# print(f)

# STARTING ASYMETTRIC!!!!!!!!!!!!!!!!!!!!!!!!!!!11

# generating private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=4096, # 2048 is a happy-medium between security and performance
)

# generating public key
public_key = private_key.public_key()



# signing the message which allows anyone with the public key to confirm attribution
message = symettric_key
signature = private_key.sign(
    message,
    padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
    
)

# encryption process
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# verification section
public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# decryption process
symettric_key_out = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("symettric_key_out", symettric_key_out)


# END ASYMETTRIC

f = Fernet(symettric_key_out)

f2 = Fernet(symettric_key_out)

print(f == f2)

plaintext = bytes("THIS IS THE NEW KEY FOR THE RADIO ~ " + str(datetime.now()), 'UTF-8')

print(plaintext)

token = f.encrypt(plaintext)

tag = create_hmac(token, symettric_key)

print("verifying key 1")

verify_hmac(token,symettric_key, tag)



print("key 1 verified")

print(token)


dec = f.decrypt(token)

print("correct timeframe" if vertifyTimestamp(dec) else "incorrect timeframe")

print(dec)

