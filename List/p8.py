# Exercise 8: Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
for i in sub_list:
    list1[2][1][2].append(i)
print('list after add:',list1)