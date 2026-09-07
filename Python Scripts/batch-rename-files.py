# pip install os (built-in, no install needed)
import os
folder = "my_files"
for i, filename in enumerate(os.listdir(folder)):
    ext = os.path.splitext(filename)[1]
    os.rename(f"{folder}/{filename}", f"{folder}/file_{i}{ext}")
print("Files renamed successfully")
