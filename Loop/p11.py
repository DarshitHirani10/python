# Exercise 12: Display Fibonacci series up to 10 terms
a=-1
b=1
c=a+b
for i in range(10):
    print(c)
    a=b
    b=c
    c=a+b