# enumerate() Function:
# This function returns a list of all active threads currently running


from threading import Thread,current_thread
from time import sleep

def display():
    print(current_thread().name,'started...')
    sleep(3)
    print(current_thread().name,'ended...')


t1=Thread(target=display,name="ChildThread1")
t2=Thread(target=display,name="ChildThread2")
t3=Thread(target=display,name="ChildThread3")
t1.start()
t2.start()
t3.start()

l = enumerate()

for t in l:
    print("Thread Name:" ,t.name)

sleep(5)

l = enumerate()
for t in l:
    print("Thread Name:" ,t.name)


