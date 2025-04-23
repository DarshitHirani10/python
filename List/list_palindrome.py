#check list is palindrome or not

list1 = []
list1.append(input("enter number: "))
list1.append(input("enter number: "))
list1.append(input("enter number: "))
list1.append(input("enter number: "))
list1.append(input("enter number: "))

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")
