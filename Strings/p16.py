# Exercise 16: Removal all characters from a string except integers
str=input("Enter a string:")
s=''
for i in str:
    if i.isdigit():
        s+=i
print(s)