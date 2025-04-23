# Exercise 14: Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print('before remove empty strings from a list of strings:',str_list)
for i in str_list:
    if i=="" or i==None:
        str_list.remove(i)
print("after remove empty strings:",str_list)