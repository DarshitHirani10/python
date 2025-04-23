# Exercise 8: Sort a tuple of tuples by 2nd item
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
d1=dict(tuple1)
t1={k:v for k,v in sorted(d1.items(),key=lambda x:x[1])}
print (tuple(t1.items()))
#also work with list