import json
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print('ENO:{}, ENAME:{}, ESAL:{}, EADDR:{}'.format(self.eno,self.ename,self.esal,self.eaddr))

e=Employee(100,'Durga',1000.0,'Hyderabad') 

emp_dict = e.__dict__

print(emp_dict)

with open('emp.json','w') as f:
    json.dump(emp_dict,f,indent=4)
    
with open('emp.json','r') as f: 
    edict = json.load(f)

#print(type(edict))
newE=Employee(edict['eno'],edict['ename'],edict['esal'],edict['eaddr'])

newE.display()