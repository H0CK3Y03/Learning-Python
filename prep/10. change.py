with open("p2.txt", "r") as file:

    new_text = ""

    for line in file:

        for letter in line:

            with open("p2.txt", "w") as file_write:

                if letter.isupper():

                    new_letter = letter.replace(letter, letter.lower())

                    new_text += new_letter

                elif letter.islower():

                    new_letter = letter.replace(letter, letter.upper())

                    new_text += new_letter

                else:

                    new_letter = letter

                    new_text += new_letter

                file_write.write(new_text)





