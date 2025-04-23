# Exercise 2: Append new string in the middle of a given string
s1='hiiy'
s2='\'between\''
s3=s1[0:len(s1)//2]+s2+s1[len(s1)//2:]
print('new string:',s3)