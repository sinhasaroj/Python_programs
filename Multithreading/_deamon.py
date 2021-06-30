# Daemon Threads:
#---> The threads which are running in the background are called Daemon Threads.
#   The main objective of Daemon Threads is to provide support for Non Daemon Threads( like main thread)
#   Eg: Garbage Collector
#   Whenever Main Thread runs with low memory, immediately PVM runs Garbage
#---> Collector to destroy useless objects and to provide free memory,so that Main Thread
#  can continue its execution without having any memory problems.
# --->We can check whether thread is Daemon or not by using t.isDaemon() method of 
#  Thread class or by using daemon property.


from threading import current_thread,Thread
import time

print(current_thread().isDaemon()) #False
print(current_thread().daemon) #False 


#-->We can change Daemon nature by using setDaemon() method of Thread class.
#                   t.setDaemon(True)
# --->But we can use this method before starting of Thread.i.e once thread started,we
#     cannot change its Daemon nature,otherwise we will get
#--->RuntimeException:cannot set daemon status of active thread.


print(current_thread().isDaemon())
# current_thread().setDaemon(True)


# output--> RuntimeError: cannot set daemon status of active thread


#  Default Nature:
#  By default Main Thread is always non-daemon.But for the remaining threads Daemon
#   nature will be inherited from parent to child.i.e if the Parent Thread is Daemon then child
# thread is also Daemon and if the Parent Thread is Non Daemon then ChildThread is also
#  Non Daemon.
def job():
    print("Child Thread")

t=Thread(target=job)
print(t.isDaemon())#False
t.setDaemon(True)
print(t.isDaemon()) #True 


# Note: Main Thread is always Non-Daemon and we cannot change its Daemon Nature b'z
# it is already started at the beginning only.

# Whenever the last Non-Daemon Thread terminates automatically all Daemon Threads will
# be terminated.

def display():
    for _ in range(10):
        print('Lazy Thread')
        time.sleep(2)


t = Thread(target=display)
t.setDaemon(True)  # this is stop the program excution once Main Thread completes its excution.

t.start()
time.sleep(4)
print('End of the the Main Thread')
