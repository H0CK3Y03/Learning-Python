import random, string

x = string.digits
y = string.ascii_letters
z = string.punctuation


pass_word = x + y + z
heslo = ""

for i in range(int(input("Dlzka hesla: "))):
    heslo += random.choice(pass_word)

print(heslo)