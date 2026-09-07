# pip install os hashlib (built-in, no install needed)
import os, hashlib
folder = "my_files"
hashes = {}
for filename in os.listdir(folder):
    path = os.path.join(folder, filename)
    with open(path, "rb") as f:
        h = hashlib.md5(f.read()).hexdigest()
    if h in hashes:
        print("Duplicate found:", filename, "==", hashes[h])
    else:
        hashes[h] = filename
print("Duplicate check completed")
