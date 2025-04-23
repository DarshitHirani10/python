# Exercise 4: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
newdict={}
for i in employees:
    newdict[i]=defaults
print(newdict)