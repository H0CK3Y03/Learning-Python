# if statement = a block of code that will execute if it's condition is true/met

age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")    #if else: isn't present, then the if statement will be skipped
#elif age == 100:                 #  "=" is an assignment operator (name = "Adam"), "==" comparison operator (does x == Y ?)
    #print("You are a century old!")   #the first condition was met, so this condition was skipped. therefore pycharm will say u r an adult instead of saying u r a century old
elif age < 0:
    print("You haven't been born yet!")   #additional conditions
else:
    print("You aren't an adult!")   #last condition