#print sum of given numbers elements
#Ex- n = 24567 , output = 2+4+5=6+7


n = input("Enter Number: ")

total = 0
i = 0

while i < len(n):
    total += int(n[i])
    i += 1
print(total)