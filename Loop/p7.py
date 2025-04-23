# Exercise 8: Print list in reverse order using a loop
l1=[12,35,56,32,12,2]
l2=[]
for i in range(len(l1)):
    l2.append(l1[len(l1)-i-1])
print('before reverse',l1)
print('after reverse',l2)