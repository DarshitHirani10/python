# Exercise 9: Parse the following JSON to get all the values of a key ‘name’ within an array

# [ 
#    { 
#       "id":1,
#       "name":"name1",
#       "color":[ 
#          "red",
#          "green"
#       ]
#    },
#    { 
#       "id":2,
#       "name":"name2",
#       "color":[ 
#          "pink",
#          "yellow"
#       ]
#    }
# ]


import json

samplejson = """[ 
   { 
      "id":1,
      "name":"darshit",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"darshit",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

data = json.loads(samplejson)
name_list = [item["name"] for item in data]
print(name_list)

# data = []
# try:
#     data = json.loads(sampleJson)
# except Exception as e:
#     print(e)

# dataList = [item.get('name') for item in data]
# print(dataList)