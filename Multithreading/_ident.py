# thread Identification number

from threading import current_thread,Thread

def display():
    print('Child Thread')

t = Thread(target=display)
t.start()

print('Main Thread Identification number:', current_thread().ident)
print('Child Thread Identification number:', t.ident)