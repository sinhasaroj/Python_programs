import json

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def __repr__(self):
#         return f'Person(name={self.name},age={self.age})'

# we will get an exception if we try to serialize the instance of the above class.

# Instead we can the following:

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name={self.name},age={self.age})'
    
    def toJson(self):
        return dict(name=self.name,age=self.age)
        # also can be returned vars(self)

p1 = Person('John',89)

print(json.dumps({"john":p1.toJson()},indent=2))