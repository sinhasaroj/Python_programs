# Creating a Thread without using any class.

from threading import *

def display():
    print(f'This code(Display function) is excuted by Child Thread: {current_thread().getName()}' ) # child thread

t = Thread(target=display) # Main Thread creates child thread object.

t.start() # MainThread starts ChildThread , Child thread is responsible to excute the display method.
print(f'This code is excuted by Main Thread: {current_thread().getName()}' ) # main Thread 


