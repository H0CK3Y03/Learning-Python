# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

name = "Bro"                #Globally scoped variable (available inside & outside functions)

def display_name():         # a region(this case it's a function)
    # name = "Code"           # locally scoped variable(inside of a function)[the function needs to be called]
    print(name)             # local scoped = available only inside this function
                            # if local name is unavailable, python calls the global name variable instead

display_name()
print(name)