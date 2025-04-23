# n = int(input("enter number: "))
# fact = 1


# for i in range (1, n+1):
#     fact *= i
# print("factorial of", n , "is: ", fact)


n = int(input("enter n: "))
def cal_fac(n):
    fact = 1
    for i in range (1, n+1):
        fact *= i
    print(fact)

cal_fac(n)