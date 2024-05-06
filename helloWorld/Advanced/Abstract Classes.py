# abstract class (ghost class)= a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

from abc import ABC, abstractmethod      # abc -> acronym for "Abstract Base Class"

class Vehicle(ABC):   # Parent class Vehicle is now inheriting from ABC class
                      # In order for a child class to inherit this parent class, it will NEED to override the abstract method -> def go(self)
    @abstractmethod   # Otherwise python will not let it be instantiated, it will not work
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")


class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")

# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()