import os

# source = "moving.txt"
source = "folder1"
# destination = "C:\\Users\\adamv\\Desktop\\moved.txt"
destination = "C:\\Users\\adamv\\Desktop\\movedfolder1"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")

except FileNotFoundError:
    print(source + " was not found")










