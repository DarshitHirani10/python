# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set

l1=[2,5,1,43,67,89]
l2=[43,5,2,56,78,4]
print('lists:',l1,l2,sep='\n')
l3=[]
for i in range(0,len(l1)):
    if l1[i] in l2:
        l3.append(l1[i])
for i in l3:
    l1.remove(i)
print('intersection:',l3)
print('after removing elements:',l1)