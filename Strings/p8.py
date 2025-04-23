# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# Write a program to find all occurrences of “USA” in a given string ignoring the case.
str=input("Enter a string:")
str=str.lower()
sub='usa'
print("occurrences:",str.count(sub))