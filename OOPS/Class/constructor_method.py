class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avj(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hello", self.name, "your avg score is: ", sum/3)

s1 = student("darshit", [99, 98, 97])
s1.get_avj()

s1.hello()

s1.name = "hirani"
s1.get_avj()