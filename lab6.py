

from cryptography.fernet import Fernet

from cryptography.hazmat.primitives import hashes, hmac



key = b'AAAAAAAAAAAAAAAA'

def create_hmac(data):
    h = hmac.HMAC(key, hashes.SHA256())
    h.update(data)
    return h.finalize()

def verify_hmac(data, tag):
    h = hmac.HMAC(key, hashes.SHA256())
    h.update(data)
    return h.verify(tag)

def main():

    image_bytes = b'asdklfjasdlkfjasldkf'
    tag = create_hmac(image_bytes)

    print(tag)
    try:
        verify_hmac(image_bytes, tag)
        print("Congratulations")
    except:
        print("Failed to verify tag")


if __name__ == '__main__':
    main()
