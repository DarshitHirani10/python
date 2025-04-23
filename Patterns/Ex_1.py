#Exercise 8: Print the following pattern
# # # # #
# # # # #
# # # # #
# # # # #

n = int(input("Enter Number: "))

for i in range (n):
    for j in range (n):
        print("#", end=" ")
    print()