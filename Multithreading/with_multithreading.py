from time import perf_counter,time,sleep
from threading import Thread

def doubles(number):
    for n in number:
        sleep(1)
        print('Double:',2*n)

def squares(number):
    for n in number:
        sleep(1)
        print('Square:',n**2)

numbers = [1,2,3,4,5,6]

begintime = perf_counter()

# doubles(numbers)
t1 = Thread(target=doubles,args=(numbers,))
# squares(numbers)
t2 = Thread(target=squares,args=(numbers,))

t1.start()
t2.start()

t1.join()
t2.join() # join method implements that the main thread will excute only 
          # after the child thread has completed it's excution.

endtime = perf_counter()

print('The total time taken:',endtime-begintime)