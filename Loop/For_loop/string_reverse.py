#Get each digit from a number in the reverse order.

n = input("Enter String: ")

x = n[::-1]
for i in x:
    print(i, end="")