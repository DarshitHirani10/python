# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
ro_nu = [47, 64, 69, 37, 76, 83, 95, 97]
s_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
re=[]
for i in ro_nu:
    if i not in s_dict.values():
        re.append(i)
for i in re:
    ro_nu.remove(i)
print('after removing:',ro_nu)