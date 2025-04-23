# Exercise 3: Print characters present at an even index number

# str = input("enter string : ")

# for i in str [::2]:
#     print(i)
 
#---------------------------------------------------------------------------

string = input("Please enter your input")
for i in string:
    if (string.index(i))%2==0:
        print(i)

#----------------------------------------------------------------------------

# str = input("Enter string: ")
# i = 0
# size = len(str)

# for i in range (i, size):
#     if(i%2 == 0):
#         print(i)
#         i += 1

#----------------------------------------------------------------------------

# word = input("Enter word: ")
# size = len(word)

# for i in range(1, size-1, 2):
#     print("index[", i, "]", word[i]) 