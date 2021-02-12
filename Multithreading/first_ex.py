import threading

print("Current Executing Thread:",threading.current_thread().getName())

# Output:  Current Executing Thread: MainThread

#  Note: threading module contains function current_thread() which returns the current
#  executing Thread object. On this object if we call getName() method then we will get
#  current executing thread name.