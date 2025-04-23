#check number prime or not

n = int(input("enter number: "))
flag = 0

for i in range(2,n):
  if n%i==0:
    flag = 1
    break
if flag == 1:
  print('Not Prime')
else:
  print("Prime")


# a = int(input("starting number: "))
# b = int(input("ending number: "))
# print("prime number between", a , "and", b , "are: ")

# for num in range (a, b):
#     if num>1:
#         for i in range (2, num):
#             if num%i == 0:
#                 break
#         else:
#             print(num)