# Synchronization By using Lock Concept:

#  Locks are the most fundamental synchronization mechanism provided by threading
# module.
#  We can create Lock object as follows l = Lock()
#  The Lock object can be hold by only one thread at a time.If any other thread required
#  the same lock then it will wait until thread releases lock. (Similar to common wash
#  rooms, public telephone booth etc)
#   A Thread can acquire the lock by using acquire() Method l.acquire()
#   A Thread can release the lock by using release() Method l.release()

#  Note: To call release() method compulsory thread should be owner of that lock.i.e thread
#  should has the lock already,otherwise we will get Runtime Exception saying
#  RuntimeError: release unlocked lock.


from threading import Thread,Lock
from time import sleep

l = Lock()

def display(name):

    l.acquire()
    
    for _ in range(10):  
        
        print('Good Evening:' ,end='',flush=True)
        sleep(2)
        print(name)

    l.release()

t1 = Thread(target=display,args=('Smith',))
t2 = Thread(target=display,args=('David',))

t1.start()
t2.start()

# This l.acquire and l.release methods stops the data incon issues.
# If we release the lock without acquiring the lock, we will get run time error.

# Problem with Simple Lock:
# The standard Lock object does not care which thread is currently holding that lock.If the
# lock is held and any thread attempts to acquire lock, then it will be blocked,even the same
# thread is already holding that lock.


l=Lock()
print("Main Thread trying to acquire Lock")
l.acquire()
print("Main Thread trying to acquire Lock Again")
l.acquire()


# Output
# D:\python_classes>py test.py
# Main Thread trying to acquire Lock
# Main Thread trying to acquire Lock Again
# --
# In the above Program main thread will be blocked b'z it is trying to acquire the lock second
# time.
