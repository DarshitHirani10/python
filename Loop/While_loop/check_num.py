# check if number is availabel in list or not

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = 16
i = 0

while i < len(nums):
    if(nums[i] == x):
        print("Found at index", i)
    else:
        print("Not Found")    
    i += 1