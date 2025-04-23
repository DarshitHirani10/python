# Exercise 4: Count the occurrence of each element from a list
l1=[12,23,45,2,5,32,12,2,23,56,32,23]
l2={}
for i in l1:
    if i not in l2:
        l2[i]=l1.count(i)
print(l2)