# Exercise 2: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
l3=[]
for i,j in zip(list1,list2):
    l3.append(i+j)
print(l3)