with open('zoznam.txt', 'r') as input_file:
    with open('otoceny_zoznam.txt', 'w') as output_file:
        for line in input_file:
            # Oddeliť priezvisko od mena pomocou medzery
            parts = line.strip().split(' ')
            # Otočenie poradia priezviska a mena
            reversed_name = f"{parts[1]} {parts[0]}"
            # Zapísať do výstupného súboru v opačnom poradí
            output_file.write(reversed_name + '\n')
