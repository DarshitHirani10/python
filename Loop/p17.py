# Exercise 17: Find the sum of the series up to n terms
# Write a program to calculate the sum of series up to n terms. For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
digit=0
sum=0
n=int(input('Enter a number: '))
for i in range(n):
    digit=digit*10+2
    sum+=digit
print('sum of series:',sum)