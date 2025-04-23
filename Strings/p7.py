# Exercise 7: String characters balance Test
# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.
s1=input("Enter a string1:")
s2=input("Enter a string2:")
count=0
for i in s1:
    if i not in s2:
        break
    else:
          count+=1
if count==len(s1):
    print("True")
else:
    print("False")