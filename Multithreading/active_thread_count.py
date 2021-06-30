# current Active Thread---active_count()

from threading import Thread,active_count,current_thread
from time import sleep


def display():
    print(current_thread().name,'started...')
    sleep(3)
    print(current_thread().name,'ended...')

print('The number of active threads:', active_count()) # 1 active thread i.e main thread

t1 = Thread(target=display,name = 'Child Thread-1')
t2 = Thread(target=display,name = 'Child Thread-1')
t3 = Thread(target=display,name = 'Child Thread-1')
t1.start()
t2.start()
t3.start()

print('The number of active threads:', active_count()) # 4 active threads i.e 3 child 1 main
sleep(4)

print('The number of active threads:', active_count()) # 1 active thread main thread


