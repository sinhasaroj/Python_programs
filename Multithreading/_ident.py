# thread Identification number ---ident


from threading import current_thread,Thread

def display():
    print('Child Thread',current_thread().ident)
    print('Child Thread Name',current_thread().name)
    print()

t = Thread(target=display,name = 'Saroj')
t.start()

print('Main Thread Identification number:', current_thread().ident)
print()
print('Child Thread Identification number:', t.ident)

