# Object Serialization by using JSON

# Importance of JSON:
# JSON --> JavaScript Object Notation

# Any programming language can understand json. Hence JSON is the most commonly used
# message format for applications irrespective of programming language and platform. It is
# very helpful for interoperability between applications.

# It is human readable format.
# It is light weight and required less memory to store data.


# Eg:
# Java Application sends request to Python application
# Python application provide required response in json form.
# Java application can understand json form and can be used based on its requirement.


# Python's json module:

# As the part of programming, it is very common requirement to convert python object into
# json form and from json form to python object. For these conversions (Serialization and
# Deserialization) Python provides inbuilt module json.


# json module defines the following important functions:

# For Serialization Purpose (From Python to JSON Form):
# 1) dumps() --> It serializes python dict object to json string.
# 2) dump() --> Converting python dict object to json and write that json to provided json
# file. It serializes to a file.

# For Deserialization Purpose (From JSON form to Python form):
# 1) loads() --> Converting JSON string to python dict. It deserializes to a string.
# 2) load() --> Reading json from a file and converting to python dict object. Deserializes
# from a json file.

import json

employee={'name':'durga',
 'age':35,
 'salary':1000.0,
 'ismarried':True,
 'ishavinggirlfriend':None
 }
json_string = json.dumps(employee, indent=2, sort_keys=True)

print(json_string)

with open('emp.json','w') as f:
    json.dump(employee,f,indent=4)

print('Serializartion completed')

