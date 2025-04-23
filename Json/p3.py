# Exercise 3: PrettyPrint following JSON data

import json

data = {"name" : "darshit", "age" : 22, "address" : "rajkot"}

prettyprintjsondata = json.dumps(data, indent=2, separators=(","," = "))
print(prettyprintjsondata)