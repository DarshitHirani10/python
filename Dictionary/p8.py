# Exercise 8: Rename key of a dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
#city to location
old="city"
new="location"
if old in sample_dict.keys():
    val=sample_dict[old]
    del sample_dict[old]    
    sample_dict.update({new:val})
print(sample_dict)