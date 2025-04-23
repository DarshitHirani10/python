# Exercise 15: Remove special symbols / punctuation from a string
import re
import string
str1=input("Enter a string:")
print('new string:',str1.translate(str1.maketrans('','',string.punctuation)))
print('new string:',re.sub(r'[^\w\s]', '', str1))