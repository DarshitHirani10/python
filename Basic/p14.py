# Exercise 14: Print a downward half-pyramid pattern of stars
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

n = 5

for i in range (n, 0, -1):
    for j in range (i, 0, -1):
        print("*", end=" ")
    print()

    