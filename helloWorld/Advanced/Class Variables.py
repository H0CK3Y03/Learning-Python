# instance variables are declared inside of the constructor(__init__), they are given unique values
# class variables are declared inside of the class, but outside of the constructor, they are default for all objects(car_n)
from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")
car_3 = Car("Peugeot", "308", 2015, "red")

# car_3.wheels = 2

Car.wheels = 2

print(car_1.wheels)
print(car_2.wheels)
print(car_3.wheels)

# print(Car.wheels)


