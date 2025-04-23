# Exercise 5: Iterate both lists simultaneously
l1 = ["Hello ", "take "," hii"]
l2 = ["Dear", "Sir"]
length=len(l1) if len(l1)>len(l2) else len(l2)
for i in range(length):
    if i<len(l1):
        print(l1[i],end='')
    if i<len(l2):
        print(l2[i])