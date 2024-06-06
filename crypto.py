from cryptography.fernet import Fernet


key = Fernet.generate_key()
f = Fernet(key)


key2 = Fernet.generate_key()
f2 = Fernet(key2)


token = f.encrypt(b"Here is my secret code!")


print(token)


dec = f.decrypt(token)


print(dec)