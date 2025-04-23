# Exercise 2: Access the value of key2 from the following JSON

import json

data = {"name" : "darshit" , "age" :  22}
jsondata = json.dumps(data)
print(data["age"])