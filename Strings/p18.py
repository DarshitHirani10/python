# Exercise 18: Replace each special symbol with # in the following string
import string
str=input("Enter a string:")
for i in string.punctuation:  
    # str=str.translate(str.maketrans(i,'#'))
    str=str.replace(i,'#')
print(str)