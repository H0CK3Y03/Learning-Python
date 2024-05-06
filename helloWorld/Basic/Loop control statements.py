# Loop Control Statements = change a loops execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop.
# pass =        does nothing, acts as a placeholder

#while True:
    #name = input("Enter your name: ")
    #if name != "":                    #   != means does not equal/ opposite to ==   does equal
        #break

phone_number = "123-456-7890"        #ctrl + /(is ? if u use shift, next to Rshift) - makes a comment
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)

for i in range(1,21):
    if i == 13:
        pass
    print(i)
