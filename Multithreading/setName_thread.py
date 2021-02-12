from threading import Thread,current_thread

print(current_thread().getName())
current_thread().setName('Saroj Sinha')
print(current_thread().getName())
# only name attribute also can be used to get the name.
print(current_thread().name)

