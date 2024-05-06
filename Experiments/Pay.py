def vyplata(euro_na_hodinu, euro_na_hodinu_nocna, typ, pocet_hodin, pocet_dni, aky_den, default_euro, sviatok):

    if typ.upper() == "R":

        euro_na_hodinu = default_euro

        if aky_den.upper() == "S":

            euro_na_hodinu = default_euro + default_euro * 0.5

        if aky_den.upper() == "N":

            euro_na_hodinu = default_euro * 2

        if sviatok.upper() == "Y":

            euro_na_hodinu = default_euro * 2


    # if typ.upper() == "N":

    #     pocet_hodin = 4
    #
    # if aky_den.upper() == "S":
    #     euro_na_hodinu = default_euro + default_euro * 0.5
    #
    # if aky_den.upper() == "N":
    #     euro_na_hodinu = default_euro * 2
    #
    # if sviatok.upper() == "Y":
    #     euro_na_hodinu = default_euro * 2


    vypocet = pocet_hodin * euro_na_hodinu * int(pocet_dni)


    return round(vypocet, 2)


default_euro = 4.981
euro_na_hodinu = 0
euro_na_hodinu_nocna = 1.609
typ = input("Ranna alebo nocna? R/N -> ")
pocet_hodin = int(input("Odrobene hodiny: "))
pocet_dni = input("Kolko dni si pracoval? ")
aky_den = input("Sobota alebo nedela? Daj enter ked nic z toho: S/N: ")
sviatok = input("Je sviatok? Y/N -> ")

if pocet_dni == "":

    pocet_dni = 1

if pocet_hodin == "" or pocet_hodin == 12:

    pocet_hodin = 11.5

vypocet = vyplata(euro_na_hodinu, euro_na_hodinu_nocna, typ, pocet_hodin, pocet_dni, aky_den, default_euro, sviatok)

with open("Plat.txt", "r") as file:

    current = float(file.read())
    print(f"Mal si: {current}")

with open("Plat.txt", "w") as file:

    new = round(current + vypocet, 2)
    file.write(str(new))

print(f"""Teraz si zarobil: {vypocet}
Celkovo mas zarobene: {new}""")
