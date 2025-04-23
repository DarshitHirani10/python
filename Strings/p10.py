# Exercise 10: Write a program to count occurrences of all characters within a string
str=input("Enter a string:")
dic={}
for i in str:
    if i not in dic.keys():
        dic[i]=str.count(i)
print(dic)