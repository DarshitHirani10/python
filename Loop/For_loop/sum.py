#print sum of first n number

n = int(input("Enter Number: "))

sum = 0
for i in range (1, n+1):
    sum += i

    print("Total sum is: ", sum)