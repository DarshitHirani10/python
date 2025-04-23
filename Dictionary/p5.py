# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
newdict={}
# Keys to extract
keys = ["name", "salary"]
for key in keys:
    if key in sample_dict.keys():
        newdict[key] = sample_dict[key]
print(newdict)