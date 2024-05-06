import string, random


def heslo():
    zet = []
    for i in range(int(input("Dlzka hesla (cislo): "))):
        y = string.printable
        zet += list(random.choice(y))
    return zet



print(heslo())
