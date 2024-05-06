# function = a block of code which is executed only when it is called

def hello(first_name,last_name,age):        # the sent arguments require the same amount of parameters(nicknames)
    print("hello "+first_name+" "+last_name)
    print("Have a nice day!")
    print("You are: "+str(age)+" years old!")


my_name = "Bro"
# hello("Adam")           # hello(this is called an argument, we are sending information to our function)
# hello("Dude")
hello("Bro","Code",21)
