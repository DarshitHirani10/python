# Exercise 3: Calculate sum of all numbers from 1 to a given number
n=int(input('Enter a number: '))
sum=0
for i in range(n+1):
    sum+=i
print('Sum of all numbers from 1 to a given number:', sum)