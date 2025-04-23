# Exercise 1A: Create a string made of the first, middle and last character
str=input("Enter a string:")
mid=((len(str))//2)
print("new string:",str[0]+str[mid]+str[-1])
# Exercise 1B: Create a string made of the middle three characters
print("middle three characters:",str[mid-1]+str[mid]+str[mid+1])