from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os



password = b"my-strong-password"          
salt = os.urandom(16)                     


kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)

key = kdf.derive(password)                

print(f"Derived Key: {key.hex()}")

# Example plaintext
plaintext = b"Secret message for encryption"

# Generate random 96-bit IV for AES-GCM
iv = os.urandom(12)

# Create Cipher object
encryptor = Cipher(
    algorithms.AES(key),
    modes.GCM(iv),
    backend=default_backend()
).encryptor()

# Encrypt
ciphertext = encryptor.update(plaintext) + encryptor.finalize()

# Authentication tag
tag = encryptor.tag

print(f"Ciphertext (hex): {ciphertext.hex()}")
print(f"Tag (hex): {tag.hex()}")
print(f"IV (hex): {iv.hex()}")
print(f"Salt (hex): {salt.hex()}")

# Decrypt the message

decryptor = Cipher(
    algorithms.AES(key),
    modes.GCM(iv, tag),
    backend=default_backend()
).decryptor()

decrypted = decryptor.update(ciphertext) + decryptor.finalize()

print(f"Decrypted text: {decrypted.decode()}")

