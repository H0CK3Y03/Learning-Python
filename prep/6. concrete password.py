import secrets, string

char = string.ascii_letters + string.punctuation

password = ""

for x in range(int(input("Number of passwords: "))):
    password = ""
    for i in range(8):
        password += secrets.choice(char)
    with open("concrete password.txt", "a") as file:
        file.write(f"{password}\n")


with open("concrete password.txt", "r") as file:
    print(file.read())
