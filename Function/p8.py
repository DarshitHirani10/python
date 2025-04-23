# # Exercise 8: Generate a Python list of all the even numbers between 4 to 30

def even4_30():
    l1=[]
    for i in range(4,30,2):
        l1.append(i)
    print(l1)
even4_30()
print(list(range(4,30,2)))