# # OOP Exercise 7: Check type of an object
# Write a program to determine which class a given Bus object belongs to.
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print('type of object:',type(School_bus))
# OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class
print('school_bus object is instance of bus?',isinstance(School_bus, Bus))
print('school_bus object is instance of vehicle?',isinstance(School_bus, Vehicle))