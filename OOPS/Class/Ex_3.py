# creating a function to add complex numbers

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def shownumber(self):
        print (self.real, "i +" , self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(7, 8)
num1.shownumber()

num2 = Complex(8, 9)
num2.shownumber()

num3 = num1 + num2
num3.shownumber()
# num3 = num1.add(num2)
# num3.shownumber()

num3 = num1 - num2
num3.shownumber()