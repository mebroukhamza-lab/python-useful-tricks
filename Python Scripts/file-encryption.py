# pip install cryptography
from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
with open("secret.txt", "rb") as f:
    data = f.read()
encrypted = cipher.encrypt(data)
with open("secret.enc", "wb") as f:
    f.write(encrypted)
print("File encrypted successfully. Keep this key safe:", key.decode())
