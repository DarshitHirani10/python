num = int(input("Enter Number: "))
n1 = -1
n2 = 1

print("Fibonacci series is: ",end=" ")
for i in range (num):
    n3 = n2 + n1
    n1 = n2
    n2 = n3
    print(n3, end=" ")
print() 