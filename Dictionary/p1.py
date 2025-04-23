# Exercise 1: Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict={}
for k in range(len(keys)):
    dict[keys[k]] = values[k]
print(dict)