# list = [1, 3, 4, 5, 1, 1, 3, 4, 1, 1, 3, 1, 1, 5, 1]

# value = 1
# count = 0
# for i in list:
#     if (i == value):
#         count = count + 1
# print(count)

#-----------------------------------------------------

list = [1, 3, 4, 5, 1, 1, 3, 4, 1, 1, 3, 1, 1, 5, 1]

dict = dict.fromkeys(list, 0)

for val in list:
    dict[val] += 1
print(dict)