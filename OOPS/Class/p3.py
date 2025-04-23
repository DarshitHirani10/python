# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    # def print_spmi(self):
    #     print("max_speed:",self.max_speed,"mileage:",self.mileage)
class Bus(Vehicle):
    def __init__(self,name,max_speed,mileage):
        super().__init__(name,max_speed,mileage)
        print("name:",self.name,"max_speed:",self.max_speed,"mileage:",self.mileage)
b1=Bus('school',100,50)