# str.format() = optional method that gives users more control when displaying output

# animal = "cow"
# item = "moon"
#
# print("The "+animal+" jumped over the "+item)

animal = "cow"
item = "moon"

# print("The {} jumped over the {}".format("cow","moon"))
# print("The {} jumped over the {}".format(animal,item))     # {} - format fields - function as a placeholder for a value or variable. They work in order.(first set of {} store first value in "x".format(value1,value2)
# print("The {} jumped over the {}".format(item,animal))
# print("The {0} jumped over the {1}".format(animal,item))     # positional argument///same as indexing
# print("The {1} jumped over the {0}".format(animal,item))
# print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))    # keyword argument
# print("The {item} jumped over the {animal}".format(animal="cow",item="moon"))
# print("The {animal} jumped over the {animal}".format(animal="cow",item="moon"))
# print("The {0} jumped over the {0}".format(animal,item))
# print("The {1} jumped over the {1}".format(animal,item))

# text = "The {} jumped over the {}"
# print(text.format(animal,item))

# str.format() = optional method that gives users more control when displaying output

name = "Bro"

# print("Hello, my name is {}. Nice to meet you".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name))   #this adds 10 spaces after the argument, this case -> name(Bro)
# print("Hello, my name is {:<10}. Nice to meet you".format(name))  #this aligns the argument to the left (this is default) so name + 10spaces
# print("Hello, my name is {:>10}. Nice to meet you".format(name))  #this aligns the argument to the right so 10spaces + name
# print("Hello, my name is {:^10}. Nice to meet you".format(name))  #this centers the argument so 5spaces + argument + 5spaces
#
# print("Hello, my name is {0:10}. Nice to meet you".format(name))  #positional argument
# print("Hello, my name is {name:10}. Nice to meet you".format(name))  #keyword argument

# num = 3.14159

# print("The number pi is {:.2f}".format(num))  #.2f  - 0.2569  -> 0.25  -> first 2 floating numbers are displayed
# print("The number pi is {:.3f}".format(num))  # .xf rounds your number to x amount of decimal points

num = 1000

print("The number is {:,}".format(num))   # thousand format (1,000,000)
print("The number is {:b}".format(num))   # binary representation of your number
print("The number is {:d}".format(num))   # default decimal
print("The number is {:o}".format(num))   # oktodecimal
print("The number is {:x}".format(num))   # hexadecimal (x - lowercase letters, X - uppercase letters)
print("The number is {:e}".format(num))   # scientific notation (e - lowercase letters, E  - uppercase letters)













































