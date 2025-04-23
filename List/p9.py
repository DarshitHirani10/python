# Exercise 9: Replace list’s item with new value if found
list1 = [5, 10, 15, 20, 25, 50, 20]
for i in list1:
    if i==20:
        list1[list1.index(i)]=200
        break
print(list1)