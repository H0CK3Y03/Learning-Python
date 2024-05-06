import string

mala_abc = string.ascii_lowercase

with open("pismena.txt", "w") as file:
    file.write(mala_abc)

with open("pismena.txt", "r") as file:
    print(file.read())