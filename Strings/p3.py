# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
s1=input("Enter a string1:")
s2=input("Enter a string2:")
mi1=((len(s1))//2)
mi2=((len(s2))//2)
s3=s1[0]+s2[0]+s1[mi1]+s2[mi2]+s1[-1]+s2[-1]
print("new string:",s3)