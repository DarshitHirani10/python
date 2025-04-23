# class Person:
#     name = "anonymous"

#     def changename(self, name):
#         self.name = name

# p1 = Person()
# p1.changename("darshit")
# print(p1.name)
# print(Person.name)

#-------------------------------------------------

# class Person:
#     name = "anonymous"

#     def changename(self, name):
#         Person.name = name

# p1 = Person()
# p1.changename("darshit")
# print(p1.name)
# print(Person.name)

#--------------------------------------------------

# class Person:
#     name = "anonymous"

#     def changename(self, name):
#         self.__class__.name = name

# p1 = Person()
# p1.changename("darshit")
# print(p1.name)
# print(Person.name)

#---------------------------------------------------

class Person:
    name = "anonymous"

    # def changename(self, name):
    #     self.name = name

    @classmethod
    def changename(cls, name):
        cls.name = name


p1 = Person()
p1.changename("darshit")
print(p1.name)
print(Person.name)