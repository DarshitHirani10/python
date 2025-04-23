# # OOP Exercise 5: Define a property that must have the same value for every class instance (object)
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

# Use the following code for this exercise.
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = 'white'

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass
c=Car('aura',150,80)
b=Bus('volvo',100,50)
print('color:', b.color,'name:', b.name,'max_speed:', b.max_speed,'mileage:',b.mileage)
print('color:',c.color,'name:',c.name,'max_speed:',c.max_speed,'mileage:',c.mileage)