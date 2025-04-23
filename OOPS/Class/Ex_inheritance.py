#single inheritance

# class car:
    
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")

# class Tata(car):

#     def __init__(self, model_name):
#         self.model_name = model_name

# c1 = Tata("Tiago")
# print(c1.model_name)

# print(c1.start())

# c2 = Tata("harrier")
# print(c2.model_name)

# print(c2.stop())

#----------------------------------------------------------------------------------

#multilevel in heritance

# class car:
    
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")

# class Tatacar(car):

#     def __init__(self, brand):
#         self.brand = brand

# class Harrier(Tatacar):

#     def __init__(self, type):
#         self.type = type

# c1 = Harrier("Electric")
# print(c1.type)
# print(c1.start())

#----------------------------------------------------------------------------------

#multiple inheritance

# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A,B):
#     varC =  "welcome to class c"

# c1 = C()

# print(c1.varC)
# print(c1.varA)
# print(c1.varB)