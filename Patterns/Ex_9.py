#hill pattern

# n = 5
# for i in range (n):
#     for j in range (i, n):
#         print(" ", end=" ")
#     for j in range (i):
#         print("", end=" ")
#     for j in range (i+1):
#         print("", end=" ")
#     print()
#     p+=1



n = 5
p = 65
for i in range (n):
    for j in range (i, n):
        print(" ", end=" ")
    for j in range (i):
        print(chr(p), end=" ")
        p += 1
    for j in range (i+1):
        print(chr(p), end=" ")
        p += 1

    print()