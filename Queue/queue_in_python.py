"""
A queue is a container that holds data. 
The data that is entered first will be removed first, and hence a queue is also called "First in First Out" (FIFO). 
The queue has two ends front and rear. The items are entered from the rear and removed from the front side.

"""

import queue

q1 = queue.Queue()
q1.put(10) # Put will additem 10 to the queue.

"""
By default, the size of the queue is infinite and you can add any number of items to it.
In case you want to define the size of the queue the same can be done as follows
"""

q1 = queue.Queue(5) #The max size is 5.
q1.put(1)
q1.put(2)
q1.put(3)
q1.put(4)
q1.put(5)
print(q1.full()) # will return true. 

# The above queue won't take more than 5 items.

"""
To remove an item from the queue, you can use the method called get(). 
This method allows items from the queue when called.
"""

q1 = queue.Queue()
q1.put(10)

item1 = q1.get()

print('\nThe item removed from the queue is ', item1)

# Last In First Out queue Example

import queue
q1 = queue.LifoQueue()
q1.put(10) 


# To remove an item from the LIFOqueue you can make use of get() method .
q1 = queue.LifoQueue()
q1.put(10)

item1 = q1.get()

print('The item removed from the LIFO queue is ', item1)


"""Adding more than one items in LIFO and FIFO Queues."""

q1 = queue.Queue()
for i in range(20):
    q1.put(i) # this will additem from 0 to 20 to the queue

# Remove an item from the FIFOqueue
q1 = queue.Queue()

for i in range(20):
    q1.put(i) # this will additem from 0 to 20 to the queue

while not q1.empty():
    print("The value is ", q1.get()) # get() will remove the item from the queue.

# Add and item in a LIFOqueue
q1 = queue.LifoQueue()
for i in range(20):
    q1.put(i) # this will additem from 0 to 20 to the queue

# Remove an item from the LIFOqueue
q1 = queue.LifoQueue()
for i in range(20):
    q1.put(i) # this will additem from 0 to 20 to the queue


while not q1.empty():
    print("The value is ", q1.get()) # get() will remove the item from the queue. 
