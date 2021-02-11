import json

d1 = {'a':100 , 'b':20}

d1_json = json.dumps(d1) # dumps the dict object to a string loads does the vice versa

print(d1_json) 
print( json.dumps(d1, indent=2)) 

d_json = '''
{
    "name":"John Clesse",
    "age":39,
    "height":4.5,
    "walksFunny":true,
    "sketches":[
        {
            "title":"Dead Parrot",
            "costars":["Saroj Sinha"]
        },
        {
            "title":"Ministry of silly walks",
            "costars":["Manoj Sinha","Smita Jha","Dorsey pathinate"]
            
        }
    ],
    "boring": null
}
'''

d = json.loads(d_json)
print(d)

