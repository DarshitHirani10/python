# Exercise 4: Sort JSON keys in and write them into a file

import json

data = {"id" : 1, "name" : "darshit", "age" : 21}

with open("data.json", "w") as write_files:
    d=json.dump(data, write_files, indent=4, sort_keys=True)

    print(d)