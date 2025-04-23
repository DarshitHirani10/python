# Exercise 5: Access the nested key ‘salary’ from the following JSON

import json

data = """{
    "company":{
        "employee":{
            "name":"darshit",
            "payble":{
                "salary":70000,
                "bonus":10000
            }
        }
    }
}"""

jsondata = json.loads(data)

print(jsondata["company"]["employee"]["payble"]["salary"])
