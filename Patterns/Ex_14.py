#  _ _ _ e _ _ _
#  _ _ e d e _ _
#  _ e d c d e _
#  e d c b c d e 
#  _ e d c d e _
#  _ _ e d e _ _
#  _ _ _ e _ _ _


n = 4

for i in range (n-1):
    for j in range (i, n):
        print(" ", end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range (i+1):
        print("*", end=" ")
    print()

for i in range (n):
    for j in range (i+1):
        print(" ", end=" ")
    for j in range (i, n-1):
        print("*", end=" ")
    for j in range (i, n):
        print("*", end=" ")
    print()

#----------------------------------------------------------------

# n = 4

# # Upper part of diamond
# for i in range(1, n+1):
#     for j in range(1, n-i+1):
#         print("9", end="")
#     for j in range(1, 2*i):
#         print("*", end="")
#     print()

# # Lower part of diamond
# for i in range(n-1,0, -1):
#     for j in range(1,n-i+1):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print("*", end="")
#     print()