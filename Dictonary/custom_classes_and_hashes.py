t1 = (1,2,3)
t2 = (1,2,3)

# print(t1 == t2)

print(hash(t1),hash(t2)) # if two objects are equal, then their hashes are as well equal.

d = {t1:100}

print(d[t1])
print(d[t2]) # both have the same hash so we can retrive the value of t1 using t2 as well.


class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person (name = {self.name},age = {self.age})'

p1 = Person('John',78)
p2 = Person('John',78)

print(p1==p2)
print(p1 is p2)

print(hash(p1),hash(p2))

persons = {p1:'John Object' , p2:'Eric object'}

for k in persons:
    print(k)

# persons[Person('John',78)]  Uncommenting this will give an KeyError 

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def __eq__(self,other):
        if isinstance(other,Person):
            return self.name == other.name and self.age == other.age
        else:
            return False



