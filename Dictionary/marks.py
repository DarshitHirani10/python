#create dict. from user input

marks = {}

a = input("enter phy: ")
marks.update({"phy" : a})

a = input("enter mat: ")
marks.update({"mat" : a})

a = input("enter che: ")
marks.update({"che" : a})

print(marks)