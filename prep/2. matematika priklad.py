operator = input("Operator (+, -, *, /): ")
first_number = int(input("First number: "))
second_number = int(input("Second number: "))




if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    result = first_number / second_number
else:
    print("Invalid input!")

with open("priklady.txt", "a") as file:
    file.write(f"{first_number} {operator} {second_number} = \n")
with open("vysledky.txt", "a") as file:
    file.write(f'{first_number} {operator} {second_number} = {result}\n')



print(result)