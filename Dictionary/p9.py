# Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
l1=sample_dict.values()
min=min(l1)
for i in sample_dict.keys():
    if sample_dict[i]==min:
        print(i)