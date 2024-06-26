# keyword arguments =   arguments preceded by an identifier when we pass them to a function
#                       The order of the arguments doesn't matter, unlike positional arguments
#                       Python knows the names of the arguments that a function receives

# def hello(first,middle,last):
#     print("Hello "+first+" "+middle+" "+last+"!")
#
# hello("Bro","Dude","Code")
# hello("Code","Bro","Dude")



def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last+"!")

hello(first="Bro",middle="Dude",last="Code")
hello(last="Code",middle="Dude",first="Bro")

def hello(lol,rtr,aaaaaa):
    print("Hello "+lol+" "+rtr+" "+aaaaaa+"!")

hello(lol="Bro",rtr="Dude",aaaaaa="Code")
hello(rtr="Code",aaaaaa="Dude",lol="Bro")