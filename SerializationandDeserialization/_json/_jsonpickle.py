# jsonpickle module:

# By using jsonpickle module we can serialize our custom class objects directly to json and
# we can deserialize json to our custom class objects directly.

# jsonpickle module is not available bydefault and we have to install explicitly.
# pip install jsonpickle

# This module contains
# 1. encode()---> To convert any object to json_string directly.
# 2. decode()---> To convert json_string to our original object.

# Demo program

import jsonpickle

class Employee:
    def __init__(self,eno,ename,esal,eaddr,isMarried):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
        self.isMarried=isMarried
    def display(self):
        print('ENO:{}, ENAME:{}, ESAL:{}, EADDR:{}, Is Married:{}'.format(self.eno,self.ename,self.esal,self.eaddr,self.isMarried)) 



e = Employee(100,'Durga',1000.0,'Hyderabad',True)  

# Serialization to String 

json_string = jsonpickle.encode(e)
print(json_string)

# Serialization to file

with open('emp.json','w') as f:
    f.write(json_string)


 #Deserialization
newEmp=jsonpickle.decode(json_string)
#print(type(newEmp))
newEmp.display()


#Deserialization From the file
with open('emp.json','r') as f:
    json_string=f.readline()
newEmp=jsonpickle.decode(json_string)
newEmp.display()


