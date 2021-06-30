# is_alive() Method:
# is_alive() method checks whether a thread is still executing or not

from threading import Thread,current_thread
from time import sleep

def display():
    print(current_thread().name,'started...')
    sleep(2)
    print(current_thread().name,'ended...')

t1 = Thread(target=display,name='Child Thread-1')
t2 = Thread(target=display,name='Child Thread-2')
t3 = Thread(target=display,name='Child Thread-3')

t1.start()
t2.start()
t3.start()

print(t1.name,'is Alive:',t1.is_alive())
print(t2.name,'is Alive:',t2.is_alive())
print(t3.name,'is Alive:',t3.is_alive())

sleep(3)

print(t1.name,'is Alive:',t1.is_alive())
print(t2.name,'is Alive:',t2.is_alive())
print(t3.name,'is Alive:',t3.is_alive())

