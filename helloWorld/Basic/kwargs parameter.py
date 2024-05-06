# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments

# def hello(first,last):
#     print("Hello "+first+" "+last)
#
# hello(first="Bro",middle="Dude",last="Code")

# def hello(**names):
#     print("Hello "+names['first']+" "+names['last'])
#
# hello(first="Bro",middle="Dude",last="Code")

def hello(**names):          # ** is important, the name can be whatever. Same goes with *.
    print("Hello ", end="")
    for key,value in names.items():
        print(value, end=" ")
hello(title= "Mr.",first="Bro",middle="Dude",last="Code")