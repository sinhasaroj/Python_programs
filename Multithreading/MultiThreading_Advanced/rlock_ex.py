# Rlock

# If the Thread calls recursive functions or nested access to resources,then the thread may
# trying to acquire the same lock again and again,which may block our thread.

# Hence Traditional Locking mechanism won't work for executing recursive functions.
# To overcome this problem, we should go for RLock(Reentrant Lock). Reentrant means the
# thread can acquire the same lock again and again.If the lock is held by other threads then
# only the thread will be blocked.

# Reentrant facility is available only for owner thread but not for other threads.

from threading import *
import time

l=RLock()
def factorial(n):
    l.acquire()
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
        l.release()
    return result

 def results(n):
    print("The Factorial of",n,"is:",factorial(n))

t1=Thread(target=results,args=(5,))
t2=Thread(target=results,args=(9,))
t1.start()
t2.start() 