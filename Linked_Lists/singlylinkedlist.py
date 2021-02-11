class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode:
            length += 1
            currentNode = currentNode.next
        return length
    
    def isListEmpty(self):
        if self.head is None:
            return True
        return False
            
        
    def insertEnd(self,newNode):
        if self.head is None:
            self.head = newNode     
        else:
            lastNode = self.head 
            while True:
                if lastNode.next is None:
                    break
                    
                lastNode = lastNode.next
            lastNode.next = newNode
            
    def insertHead(self,newNode):
        
        temp = self.head
        
        self.head = newNode
        self.head.next = temp
        del temp
        
    def insertAt(self,newNode,position):
        
        if position < 0 or position > self.listLength():
            print('Invalid Linked List')
            return 
        
        if position == 0: # if the position is equal to 0.
            self.insertHead(newNode)
            return
        
        currentNode = self.head # Traverse
        currentPosition = 0 # keep the track of the position
        
        while True:
            
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break   
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1
            
    def deleteHead(self):
        
        if self.isListEmpty() is False:
            temp = self.head
        
            self.head = self.head.next
            temp.next = None
            
        else:
            print(f'List is Empty, Deletion Failed')        
    def deleteEnd(self):
        
        if self.isListEmpty() is False:
            
            if self.head.next is None:
                self.deleteHead()
                return
            lastNode = self.head

            while lastNode.next:
                previousNode = lastNode
                lastNode = lastNode.next

            previousNode.next = None
        else:
            print(f'List is Empty, Deletion Failed')
            
    def deleteAt(self,position):
        
        if position < 0 or position >= self.listLength():
            print('Invalid Linked List')
            return 
        
        if self.isListEmpty() is False:
            if position == 0:
                self.deleteHead()
                return
        
            currentNode = self.head
            currentPosition = 0

            while True:

                if currentPosition == position:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    break
                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1
            
            
          
    def printList(self):
        
        temp = self.head
        
        if temp is None:
            print('List is Empty!')
            return
        
        while temp:
            print(temp.data)
            temp = temp.next

llist = LinkedList()

firstNode = Node(1)
llist.insertEnd(firstNode)
secondNode = Node(2)
llist.insertEnd(secondNode)
thirdNode = Node(3)
llist.insertEnd(thirdNode)

# llist.printList()


# llist.deleteHead()

# fourthNode = Node(4)
# llist.insertHead(fourthNode)

# fifthNode = Node(50)
# llist.insertAt(fifthNode,10)

llist.deleteAt(3)

llist.printList()


