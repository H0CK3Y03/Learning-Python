
# with open('C:\\Users\\adamv\\Desktop\\test.txt') as file:
#     print(file.read())
#
# print(file.closed)

# try:
#     with open('C:\\Users\\adamv\\Desktop\\test.tx') as file:
#         print(file.read())
# except FileNotFoundError as e:
#     print(e)
#     print("That file was not found")

try:
    with open('C:\\Users\\adamv\\Desktop\\test.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("That file was not found")





