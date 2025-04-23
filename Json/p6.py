# Exercise 6: Convert the following Vehicle Object into JSON

import json
from json import JSONEncoder

class vehical():
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class vehicalencoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
    
v1 = vehical("tata", "2.5L", "30,00,000")
v2 = vehical("tata", "2.5L", "30,00,000")

v1json = json.dumps(v1, indent=4, cls=vehicalencoder)
print(v1json)
v2json = json.dumps(v2, indent=4, cls=vehicalencoder)
print(v2json)