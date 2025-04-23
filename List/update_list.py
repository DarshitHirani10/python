#update list

x = ("1", "2", "3", "4", "5", "6", "7")
y = list(x)
y[6] = "10"
x = tuple(y)
print(x)