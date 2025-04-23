# Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set

l1={2,5,43}
l2={43,5,56,2,4}
print('set1 is subset of set2:',l1.issubset(l2))
print('set2 is subset of set1:',l2.issubset(l1))
print('set1 is superset of set2:',l1.issuperset(l2))
print('set2 is superset of set1:',l2.issuperset(l1))
if l1.issubset(l2):
    l1.clear()
else:
    l2.clear()
print('set1:',l1)
print('set2:',l2)
