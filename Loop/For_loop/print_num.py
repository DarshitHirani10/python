#find number from list 

#nums = [1, 4, 8, 16, 25, 36, 49, 64, 81, 100]

#for el in nums:
#    print(el)

#------------------------------------------------#

nums = [1, 4, 8, 16, 25, 36, 49, 64, 81, 100, 16]

x = 16

idx = 0
for el in nums:
    if(el == x):
        print("Number Found at idx", idx)
    idx += 1