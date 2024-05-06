# *args =   parameter that will pack all arguments into a tuple. * then anything we want eg. *names
#                 useful so that a function can accept a varying amount of arguments

# def add(num1,num2):
#     sum = num1 + num2
#     return sum
#
# print(add(1,2,3))

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
# print(add(1,2,3,4,5,6,7,8,9,10))

def add(*stuff):
    sum = 0
    stuff = list(stuff)       #type casting a tuple into a list so we can change shit
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8,9,10))
