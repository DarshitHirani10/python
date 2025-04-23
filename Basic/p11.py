# Exercise 11: Get each digit from a number in the reverse order.

n = int(input("enter number: "))

while n > 0:
    digit = n % 10
    n = n//10

    print(digit , end=" ")