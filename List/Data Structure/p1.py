# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second

l1=[2,5,1,43,67,89]
l2=[34,5,2,56,78,4]
l3=[]
l1=[l1[i] for i in range(1,len(l1),2)]
l2=[l2[i] for i in range(0,len(l2),2)]
l3=l1+l2
print('list1:',l1)
print('list2:',l2)
print('new list:',l3)