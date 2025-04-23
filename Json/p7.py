# Exercise 7: Convert the following JSON into Vehicle Object

import json

data ='{"company_name": "tata", "model_name": "nexon", "price": "10,00,000"}'

class vehical:
    def __init__(self, company_name, model_name, price):
        self.company_name = company_name
        self.model_name = model_name
        self.price = price

    def show(self):
        print("{self.company_name} {self.model_name} {self.price}")

vehical_dict = json.loads(data)

v1 = vehical(vehical_dict["company_name"], vehical_dict["model_name"], vehical_dict["price"])

v1.show()

# print(vehical_dict)