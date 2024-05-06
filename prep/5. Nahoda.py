import string
import secrets


chars = string.digits + string.punctuation + string.ascii_letters

password = ''

for i in range(int(input("Number of password characters: "))):
    password += secrets.choice(chars)

with open("nahoda.txt", "w") as file:
    file.write(f"{password}\n")

with open("nahoda.txt", "r") as file:
    print(file.read())