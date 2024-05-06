with open("zoznam.txt", "r") as file:

    # names = file.read()   # this basically turns the file into one string

    # for line in names:
    #     print(line)   # this prints letters
    #
    # for line in file:  # basically makes a list of strings separated by new line characters I think
    #     print(line)  # this prints everything up to a new line character as far as I'm concerned

    count = 0
    max_length = 0
    longest_name = ""
    # longest_names = []

    for line in file:

        if line[0].upper() == "T":

            count += 1

            print(line)

        length = len(line[:line.find(" ")]) + len(line[line.find(" ") + 1:])

        if length >= max_length:

            max_length = length

            longest_name = line

            # longest_names += [line[:-1]]

    print(f"""\nNumber of names beginning on \"T\": {count},
length of the longest name: {max_length},
The longest name: {longest_name}""")

