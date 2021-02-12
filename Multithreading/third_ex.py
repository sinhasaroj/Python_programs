# Creating a Thread without using any class.


from threading import *

def display():
    for i in range(10):
        print('Child Thread')

t = Thread(target=display)  #creating Thread object
t.start()                   #starting of Thread 
for i in range(10):
    print('Main Thread')