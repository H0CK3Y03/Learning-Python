# count = 0
#
# with open("p1.txt") as text:
#
#     for line in text:
#
#         for letter in line:
#
#             print(letter)
#
#             if "t" in letter or "T" in letter:
#
#                 count += 1
#
# print(count)

count = 0
chosen = input("Gimmme a lowercase letter: ")

with open("p1.txt") as text:

    for line in text:

        for letter in line:

            print(letter)

            if chosen in letter.lower() or chosen in letter.upper():

                count += 1

print(count)
