import string, random

z = ""
for i in range(int(input("Dlzka hesla (cislo): "))):
    y = random.choice(string.printable)
    z += y
x = list(z)



print(str(x))