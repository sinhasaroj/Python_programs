# If multiple threads are executing simultaneously then there may be a chance of data
# inconsistency problems.


from threading import Thread
from time import sleep

def wish(name):
    for _ in range(10):
        print('Good Evening:',end='',flush=True)
        sleep(2)
        print(name)

t1 = Thread(target=wish,args=('Saroj',))
t2 = Thread(target=wish,args=('Manoj',))
t1.start()
t2.start()



# Output
# Good Evening:Good Evening:Yuvraj
# Dhoni
# Good Evening:Good Evening:Yuvraj
# Dhoni
# ....



#  We are getting irregular output b'z both threads are executing simultaneously wish()
# function.
#  To overcome this problem we should go for synchronization.
#  In synchronization the threads will be executed one by one so that we can overcome
# data inconsistency problems.

#  Synchronization means at a time only one Thread
# The main application areas of synchronization are
# 1) Online Reservation system
# 2) Funds Transfer from joint accounts etc
 
# In Python, we can implement synchronization by using the following
# 1) Lock
# 2) RLock
# 3) Semaphore