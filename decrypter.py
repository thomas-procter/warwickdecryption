import base64
import time
from cryptography.fernet import Fernet

def decrypt1():
    file=open("key.key", "rb")
    key = file.read()
    file.close()
    with open("cyber1.txt", "rb") as f:
       data = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    with open("cyber1DECRYPTED.txt", "wb") as f:
        f.write(decrypted)

def decrypt2():
    file=open("key.key", "rb")
    key = file.read()
    file.close()
    with open("cyber2.txt", "rb") as f:
       data = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    with open("cyber2DECRYPTED.txt", "wb") as f:
        f.write(decrypted)


decrypt1()
decrypt2()

print("Decrypting...")
time.sleep(2)
print("Files decrypted...")
input("Press Enter to continue...")
