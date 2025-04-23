# Exercise 16: Calculate the cube of all numbers from 1 to a given number
n=int(input('Enter a number: '))
for i in range(1,n+1):
    cube=1
    for j in range(3):
        cube*=i
    print('current number is',i,'it\'s cube is',cube)