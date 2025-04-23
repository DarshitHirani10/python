#find number is odd or even using for loop
#print first 10 multiple of n number using for loop

#------------------------------------------------------------------------------------#
# odd
#for i in range (1, 100, 2):
#    print(i)

#even
#for i in range (2, 100, 2):
#    print(i)

#1 to 100
#for i in range (1, 101):
#    print(i)

#100 to 1
#for i in range (100, 0, -1):
#    print(i)

#multiplication table of n
n = int(input("Enter Number: "))

for i in range(1, 11):
    print(n, "*", i, "=", n*i)