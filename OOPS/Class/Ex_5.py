# define Employee class with attributes role, department & salary. this class also has a showdetails() method
#create an engineer class the inherits properties from Employee & has additional attributes : name & age

class Employee():
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showdetails(self):
        print("role= ", self.role)
        print("dept= ", self.dept)
        print("salary= ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
#        super().__init__("Engineer", "Backend Developer", "50,000")

    def showdetails(self):
        print("name= ", self.name)
        print("age= ", self.age)


engg1 = Engineer("Darshit", "21")
engg1.showdetails()
e1 = Employee("Engineer", "Backend Developer", "50,000")
e1.showdetails()

