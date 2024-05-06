# Higher Order Function = a function that either
#                         1. accepts a function as an argument
#                                        or
#                         2. returns a function
#                         (In Python, functions are also treated as objects)


# 1. :
# def loud(text):
#     return text.upper()
#
# def quiet(text):
#     return text.lower()
#
# def hello(func):           # Higher order function
#     text = func("Hello")
#     print(text)
#
# hello(loud)
# hello(quiet)

# 2. : ----------------------------------------------------------------------

def divisor(x):          # Divisor -> number that divides a different number (dividend)
    def dividend(y):      # Dividend -> number that is divided by a different number (divisor)
        return y / x
    return dividend

divide = divisor(2)    # divisor(2) returns the memory address of dividend(y) so divide is now dividend(y)
print(divide(10))

print(divisor(2)(10))
print(divisor(2))






