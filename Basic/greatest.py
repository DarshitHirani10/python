a = int(input("Enter Number: "))
b = int(input("Enter Number: "))
c = int(input("Enter Number: "))
d = int(input("Enter Number: "))


if(a>b and a>c and a>d):
    print("the greatest no. is: ",a)
elif(b>c and b>d):
    print("the greatest no. is: ",b)
elif(c>d):
    print("the greatest no. is: ", c)
else:
    print("the greatest no. is: ", d)