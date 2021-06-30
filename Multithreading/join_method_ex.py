# join() method ---> If a thread wants to wait until completing some 
#                    other thread then we should go for join() method.

from threading import Thread,current_thread
import time

def display():
    for _ in range(10):
        print('Seetha Thread')
        time.sleep(3)

t1 = Thread(target=display)
t1.start()
t1.join(10)    # this thread excuted by main thread, main thread 
             # will enter into waiting state till child thread completion. 

for _ in range(10):
    print('Main Thread')


