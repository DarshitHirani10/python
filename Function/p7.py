# Exercise 7: Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.
def display_student(name,age):
    print('name:',name,'age:',age)
display_student('darshit',19)
show_tudent=display_student
show_tudent('copy',0)