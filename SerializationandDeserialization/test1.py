# The process of converting an object from python supported form to either file supported
# form or network supported form, is called serialization (Marshalling or pickling)..

# The process of converting an object from either file supported form or network supported
# form to python supported form is called deserialization (Unmarshalling or unpickling)...

# Object Serialization by using Pickle
# Object Serialization by using JSON
# Object Serialization by using YAML


# Object Serialization by using Pickle:
# We can perform serialization and deserialization of an object wrt file by using pickle
# module. It is Python's inbuilt module.

# pickle module contains dump() function to perform Serialization(pickling).
# pickle.dump(object,file)

# pickle module contains load() function to perform Deserialization (unpickling).
# object = pickle.load(file)

import pickle

class Employee:

    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr 

    def display(self):
        print(f'Employee Number:{self.eno} , Employee Name:{self.ename} ,Employee Salary:{self.esal} , Employee Address:{self.eaddr}')


e = Employee(100,'Saroj',123,'Mumbai')

# Serialization
with open('emp.dat','wb') as f:
    pickle.dump(e,f)

print('Pickling of the object completed...')

# Deserialization

with open('emp.dat','rb') as f:
    emp_object = pickle.load(f)


print('Unpickling of the object completed')

emp_object.display()






