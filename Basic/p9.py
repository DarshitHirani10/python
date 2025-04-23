# Exercise 9: Check Palindrome Number

# n = input("Enter: ")

# if n == n[::-1]:
#     print("palindrome")
# else:
#     print("Not palindrome")

#-----------------------------------------------------------------

# string palindrome

# s = input("enter string: ")
# revstr = "" 

# for i in s:
#     revstr = i + revstr
#     print(revstr)
    
# print("reversed string is: ", revstr)

# if( s == revstr):
#     print("this string is palindrome")
# else:
#     print("this string is not palindrome")

#------------------------------------------------------------------

# number palindrome

n = int(input("Enter Number: "))

temp = n
reverse = 0 

while(n > 0):
    digit = n%10  
    reverse = reverse*10 + digit 
    n = n//10 
 
print(reverse)

if (temp != reverse):
    print("Number is not palindrome")

else:
    print("Number is palindrome")