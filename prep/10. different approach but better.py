with open("exp.txt", "r") as file:

    new_text = ""
    text = file.read()

    for letter in text:

        if letter.isupper():

            new_text += letter.lower()

        elif letter.islower():

            new_text += letter.upper()

        else:

            new_text += letter

with open("exp.txt", "w") as file_write:

    file_write.write(new_text)





