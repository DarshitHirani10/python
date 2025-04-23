#      A
#     1 2
#    B C D
#   3 4 5 6
#  E F G H I 


# n = 5
# p = 65
# num = 1

# for i in range(n):
#     print(" " * (n - i - 1), end="")

#     for j in range(i + 1):
#         if i % 2 == 0:
#             print(chr(p), end=" ")
#             p += 1

#         else:
#             print(num, end=" ")
#             num += 1

#     print()


n = 5
p = 65
num = 1

for i in range (n):
    
    for j in range (i, n):
        print("", end=" ")

    for j in range(i + 1):
        if (i%2 == 0):
            print(chr(p),end=" ")
            p += 1

        else:
            print(num, end=" ")
            num += 1

    print()