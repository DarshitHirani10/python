# Exercise 10: Remove all occurrences of a specific item from a list.
l1 = [5, 20, 15, 20, 25, 50, 20]
for i in l1:
    if l1.count(i)>1:
        for j in range(l1.count(i)):
            l1.remove(i)
print(l1)