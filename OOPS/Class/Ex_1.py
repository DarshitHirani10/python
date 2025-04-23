# class car:
#     color = "black"
#     brand = "bmw"
#     model = "m5"

# c1 = car()
# print(c1.color)
# print(c1.brand)
# print(c1.model)

#----------------------------------------------------------------

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student to the database..")

# s1 = student("darshit", 100)
# print(s1.name, s1.marks)

# s2 = student("rohit", 00)
# print(s2.name, s2.marks)

#---------------------------------------------------------------

# class student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def welcome(self):
#         print("welcome student", self.name)
#     def get_age(self):
#         return self.age
#     def get_marks(self):
#         return self.marks
    
# s1 = student("darshit", 21, 100)
# s1.welcome()
# print(s1.get_marks)

#-----------------------------------------------------------------

# class student():
#     def __init__(self, name):
#         self.name = name
    
# s1 = student("darshit")
# print(s1.name)
# del s1
# print(s1.name)

#-------------------------------------------------------------------