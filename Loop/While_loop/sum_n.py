#print sum of first n numbers using while loop

n = int(input("Enter Number: "))

sum = 0
i = 1

while i <= n :
    sum += i
    i += 1

print("The sum of first", n, "number is: ", sum)