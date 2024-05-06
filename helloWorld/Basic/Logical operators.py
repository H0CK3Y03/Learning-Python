# logical operators (and,or,not) = used to check if two or more conditional statements is true, except for not - it checks 1 and more

temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):    #If the variable is not in the range then it will print the below - for the if function to work, the temp needs to be <0 or 30< (so not in range)
    print("The temperature is bad today!")
    print("Stay inside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today!")
    print("Go outside!")

