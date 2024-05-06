# exception = events detected during execution that interrupt the flow of a program


try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:   # as e  -> e is not necessary, just standard practice(could be q for.example.)
    print(e)
    print("You can't divide by zero idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:         # Exception catches all exceptions, so last resort basically
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")






















































































