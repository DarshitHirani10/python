# Exercise 6: Copy specific elements from one tuple to a new tuple
# Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
tuple1 = (11, 22, 33, 44, 55, 66)
l2=[]
for i in tuple1:
    if i==44 or i==55:
        l2.append(i)

print(tuple(l2))
#print(tuple1[3:5])