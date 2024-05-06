# Lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time / or only one use, then planning to throw-away)
#
# lambda parameters:expression    -> syntax

double = lambda x:x * 2
multiply = lambda x, y:x * y
add = lambda x, y, z:x + y + z
full_name = lambda first_name, last_name: first_name +" "+last_name
age_check = lambda age:True if age >= 18 else False

print(double(5))
print(multiply(5,6))
print(add(24,54,30))
print(full_name("Bro", "Code"))
print(age_check(18))











