# Calculate the sum and average of the digits present in a string
str=input("Enter a string:")
sum=0
count=0
for i in str:
    if i.isdigit():
        sum+=int(i)
        count+=1
print("sum:",sum,"and average:",sum/count)