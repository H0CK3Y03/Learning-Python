import os

# path = "C:\\Users\\adamv\\Desktop\\test2.txt"
path = "C:\\Users\\adamv\\Desktop\\folder"     #double backslashes because it acts as an escape sequence for a backslash
                                               # basically \n is a new line but \\n is printed as '\n', not a new line
if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist")


























































































