# Exercise 10: Check if all items in the tuple are the same
tuple1 = (45, 45, 45, 45)
leng=len(tuple1)
if leng==tuple1.count(tuple1[0]):
    print('all same')
else:
    print('different')