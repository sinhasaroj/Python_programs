# Creating a Thread by extending Thread class

from threading import *

class My_Thread(Thread):
    def run(self):
        for j in range(10):
            print('Child-Thread')

t = My_Thread()
t.start()
for i in range(10):
    print('Main-Thread')

# The code inside run method is treated as child thread.