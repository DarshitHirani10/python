# xercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
l1 = [87, 45, 41, 65, 94, 41, 99, 94]
for i in l1:
    if l1.count(i)>1:
        l1.remove(i)
print("unique list:",l1)
tupel=tuple(l1)
print("tuple:",tupel)
print("maximum number:",max(tupel))
print("minimum number:",min(tupel))