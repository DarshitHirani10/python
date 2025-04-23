# Exercise 5: Swap two tuples in Python
tuple1 = (11, 22)
tuple2 = (99, 88)
print('before swap:',tuple1,tuple2)
temp=tuple1
tuple1=tuple2
tuple2=temp
#tuple1,tuple2=tuple2,tuple1
print('after swap:',tuple1,tuple2)