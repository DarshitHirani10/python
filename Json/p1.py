# Exercise 1: Convert the following dictionary into JSON format
 
import json

data = """{"name" : "darshit" , "age" :  22}"""

jsondata = json.loads(data)#dumps(data)
print(jsondata)