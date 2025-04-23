# Exercise 15: Get an int value of base raises to the power of exponent

b=int(input('Enter base:'))
p=int(input('Enter power:'))
ans=1
for i in range(p):
    ans*=b

print(ans)