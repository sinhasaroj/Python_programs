# Creating a Thread without extending Thread class

from threading import Thread,current_thread

class Test:
    def display(self):
        for _ in range(10):
            print("Child ",current_thread().getName())
            
obj=Test()

t1=Thread(target=obj.display)
t2=Thread(target=obj.display)
t3=Thread(target=obj.display)
t4=Thread(target=obj.display)

t1.start()
t2.start()
t3.start()
t4.start()

