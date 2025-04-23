# Exercise 4: Arrange string characters such that lowercase letters should come first
str=input("Enter a string:")
lower=''
upper=''
for i in str:
    if i.islower():
        lower+=i
    else:
        upper+=i
print('new string:',lower+upper)