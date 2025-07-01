# Advanced-encryption-Standards
Advanced Encryption Standard (AES) is a symmetric encryption algorithm used to securely encrypt and decrypt data using the same secret key. It operates on fixed-size blocks (128-bit) and supports key sizes of 128, 192, or 256 bits, making it both fast and secure for protecting sensitive data across networks, files, and APIs.
_______________________________________________
1. Key Derivation with PBKDF2
A password (b"my-strong-password") is defined, and a random 16-byte salt is generated using os.urandom(16).
The salt is used so that different keys are produced even when the same password is provided, helping to defend against precomputed attacks.
A key derivation function (PBKDF2) with SHA-256 and 100,000 iterations is configured to make brute-force attacks slower.
A 32-byte (256-bit) encryption key is derived from the password and salt using:key = kdf.derive(password)
The derived key is printed in hexadecimal format.
________________________________________________
2. Encryption with AES-GCM
A plaintext message is defined, and a 12-byte random IV (Initialization Vector) is generated using os.urandom(12).
AES-GCM is chosen because both confidentiality and integrity are provided by it.
A cipher object is created for AES in GCM mode, and an encryptor context is obtained
The plaintext is encrypted into ciphertext.
An authentication tag is produced, which ensures the integrity and authenticity of the data during decryption.
_________________________________________________
3. Decryption
A decryptor object is created with the same key, IV, and authentication tag.
The ciphertext is decrypted, and the original plaintext is recovered.
If the data had been altered, decryption would have failed with an error.
________________________________________________
Output
The derived key, ciphertext, authentication tag, IV, and salt are all displayed in hex format.
The decrypted text is printed to confirm that encryption and decryption worked successfully.
