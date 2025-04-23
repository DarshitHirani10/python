# Exercise 14: Reverse a integer number
n=int(input('Enter a number: '))
rem=0
rev=0
a=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    # print('rem',rem,'rev',rev)
    n=n//10
print('before reverse',a)
print('after reverse',rev)