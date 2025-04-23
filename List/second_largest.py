# list = [10, 20, 3, 4, 37, 86, 90, 5, 67, 65, 31, 36, 80, 100, 1]
# list.sort()


# second_largest = list[-2]
# print(second_largest)



def second_largest(list):
    large = max(list)
    list.remove(large)
    large = max(list)
    return large

li = []
n = int(input("enter size of list: "))
for i in range (0, n):
    e = int(input("enter element of list: "))
    li.append(e)

print("second largest in", li, "is: ")
print(second_largest(li))