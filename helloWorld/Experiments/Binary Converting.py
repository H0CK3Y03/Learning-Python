number = int(input("Your number please: "))

def convert(number):
    binary_number = 0
    while number >= 1:
        remainder = number % 2
        binary_number += remainder
    print(binary_number)














