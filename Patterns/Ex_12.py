# 1 2 3 4
#  A B C 
#   5 6
#    D

n = 4
p = 65
num = 1

for i in range (n):
    
    for j in range (i):
        print(" ", end="")

    for k in range (4 - i):
        if (i%2 == 0):
            print(num, end=" ")
            num += 1

        else:
            print(chr(p), end=" ")
            p += 1

    print()