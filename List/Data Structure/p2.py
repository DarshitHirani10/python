# Exercise 2: Remove and add item in a list

l1=[23,445,12,3,4,56,21]
print('before remove atnything',l1)
reindex=4
element=l1.pop(4)
print('after remove at reindex',l1)
l1.insert(2,element)
print('after add it in 2nd index',l1)
l1.append(element)
print('after adding at last',l1)