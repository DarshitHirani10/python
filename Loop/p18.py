# Exercise 18: Print the following pattern
# Write a program to print the following start pattern using the for loop

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
m=0
k=5
n=1
for i in range(9):
    if i>=5:
        m=4
        k=i-5-1
        n=-1
    else:
        k=i

    for j in range(m,k+1,n):
        print('*',end=' ')
    print()
    