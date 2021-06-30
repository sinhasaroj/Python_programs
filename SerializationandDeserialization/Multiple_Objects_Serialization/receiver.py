#Receiver is responsible to deserialize Employee objects 

import pickle

f = open('emp.dat','rb')
print('Deserializing Employee objects and printing data...') 
print()

while True:
    try:
        py_object = pickle.load(f)
        py_object.display()
    except EOFError:
        print()
        print('All employees object deserilzation completed...')
        break