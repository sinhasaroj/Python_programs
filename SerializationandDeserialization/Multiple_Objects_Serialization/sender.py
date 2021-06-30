#Sender is responsible to save Employee objects to the file 

import pickle
from emp import Employee

f = open('emp.dat','wb')
while True:
    eno = int(input('Enter the employee Number: '))
    ename = input('Enter the employee Name: ')
    esal = float(input('Enter the employee Salary: '))
    eaddr = input('Enter the employee adress: ')

    e = Employee(eno,ename,esal,eaddr)
    pickle.dump(e,f)

    option = input('Do you want to enter some more Employee object [Yes|No]:')
    if option.lower() == 'no':
        break
    
print()
print('All employees serialized...')


