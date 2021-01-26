import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

personalID = str(input("Please input the candidate's UCAS Personal ID for their University of Warwick application: "))

password = personalID.encode()

salt = b'x\xc8\xe4!\xd9wh\xa5\xdfdu\x839\xae\xb7\xf7'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))

file = open("key.key", "wb")
file.write(key)
file.close()

print("Please proceed to run the decrypt python script.")
input("Press Enter to continue...")
