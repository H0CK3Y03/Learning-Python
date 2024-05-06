class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):

    def eat(self):    # methodname(methodparameters) -> this is a method signature -> eat(self)
        print("This rabbit is eating a carrot")    # something similar to the python LEGB rules

rabbit = Rabbit()
rabbit.eat()






