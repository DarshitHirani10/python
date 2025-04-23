# Exercise 17: Find words with both alphabets and numbers
str=input("Enter a string:")
l1=str.split(' ')
l2=[]
for i in l1:
    if any(j.isalpha() for j in i) and any(j.isdigit() for j in i):
        l2.append(i)
print(i for i in l2)