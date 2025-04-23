class Car:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class Tata(Car):

    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
#        super().start()

c1 = Tata("harreir", "electric")
print(c1.type)
print(c1.start())