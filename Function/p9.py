# Exercise 9: Find the largest item from a given list
l1=[34,2,4,34,67,1,56]
max=l1[0]
for i in l1:
    if max<i:
        max=i
print('Max:',max)