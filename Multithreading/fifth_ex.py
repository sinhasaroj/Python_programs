# Creating a Thread without extending Thread class

from threading import *
class Test:
    def display(self):
        for i in range(10):
            print("Child Thread-2")
            
obj=Test()
t=Thread(target=obj.display)
t.start()
for i in range(10):
    print("Main Thread-2")