# Exercise 7: Print the following pattern
# Write a Python program to print the reverse number pattern using a for loop.

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
for i in range(6):
    for j in range(i,5):
        print(5-j,end=' ')
    print()