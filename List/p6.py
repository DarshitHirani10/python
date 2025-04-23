# Exercise 6: Remove empty strings from the list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print('before remove empty strings from a list of strings:',str_list)
for i in str_list:
    if i=="" or i==None:
        str_list.remove(i)
print("after remove empty strings:",str_list)
#you can also visit PYnative website for more learn