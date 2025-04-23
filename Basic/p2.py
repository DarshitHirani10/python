# Exercise 2: Print the Sum of a Current Number and a Previous number


previous_no = 0

for i in range (1, 11):
    sum = previous_no + i
    print("sum of", previous_no, "and", i , "=", sum)
    previous_no = i  




# print("Printing current and previous number and their sum in a range(10)")
# previous_num = 0

# for i in range(1, 11):
#     x = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x)
#     previous_num = i  