# Exercise 5: Create a Python set such that it shows the element from both lists in a pair you can use zip()
l1=[2,5,1,43,67,89]
l2=[34,5,2,56,78,4]
temp=()
sety=[]
s3=[]
length=len(l1) if len(l1)>len(l2) else len(l2)
for i in range(length):
    s3=[]
    if i<len(l1):
        s3.append(l1[i])
    if i<len(l2):
        s3.append(l2[i])
    temp=tuple(s3)
    sety.append(temp)
print(sety)
sety=set(sety)
print('new set:',sety)