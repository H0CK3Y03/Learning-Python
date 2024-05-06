class Car:    # common naming convention -> capitalizing the class name (car -> Car)
    wheels = 4          # class variables(general attributes), each object will have their own copy of this variable


    def __init__(self, make, model, year, color):  #We only pass in 4 arguments, because in Python the self argument is passed in automatically #the __init__ method wil construct objects for us (in other programming languages it's called the constructor)
        self.make = make            # individual atrributes / instance variable
        self.model = model          # instance variable
        self.year = year            # instance variable
        self.color = color          # instance variable

    def drive(self):                      #methods, drive(self) refers to the drive method that the object (Car) is using
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")