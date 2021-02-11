class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None

    def listLength(self):
        # 10-->20 -- length = 2
        length = 0

        currentNode = self.head

        while currentNode:
            currentNode = currentNode.next
            length += 1
        return length

    def isListEmpty(self):
        if self.head is None:
            return True
        return False


    def insertHead(self,newNode):

        previousHead = self.head  # Here, we store the head node as temporary node
        self.head = newNode       # made the new node as head node
        self.head.next = previousHead
        previousHead.previous = self.head
        
    def insertEnd(self,newNode):
        if self.head is None:
            self.head = newNode
            return 
        
        currentNode = self.head
        
        while True:
            if currentNode.next is None:
                break
            currentNode = currentNode.next
        currentNode.next = newNode
        newNode.previous = currentNode

    def insertAt(self,newNode,position):
        # 10 --> 30--> 20 || position == 1
        if position < 0 or position > self.listLength():
            print(f'Invalid Input, Insertion failed')
            return 

        if position is self.listLength():
            self.insertEnd(newNode)
            return

        if position == 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0

        while True:
            if currentPosition == position:
                currentNode.previous.next = newNode
                newNode.previous = currentNode.previous
                newNode.next = currentNode
                currentNode.previous = newNode
                break
            currentNode = currentNode.next
            currentPosition += 1

    def deleteEnd(self):

        if self.isListEmpty() is False:
            if self.head.next is None:
                self.deleteHead()
                return
            currentNode = self.head
            while True:
                if currentNode.next.next is None:
                    currentNode.next.previous = None
                    currentNode.next.next = None
                    currentNode.next = None
                    break

                currentNode = currentNode.next 
        else:
            print(f'List is Empty, Deletion Failed')

    def deleteHead(self):
        # 10-->20-->30
        if self.isListEmpty() is False:
            self.head = self.head.next
            self.head.previous.next = None
            self.head.previous = None

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
                    currentNode.previous.next = currentNode.next
                    currentNode.next.previous = currentNode.previous
                    currentNode.next = None
                    currentNode.previous = None
                    break

                currentNode = currentNode.next
                currentPosition += 1   
             

    def printList(self):
        
        if self.head is None:
            print('List is empty')
            return 
        currentNode = self.head
        print()
        print("Printing from the beginning of the list")
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            if currentNode.next is None:
                reverseTraversalNode = currentNode
            currentNode = currentNode.next
        print()
        print("Printing from the end")
        while True:

            if reverseTraversalNode is None:
                break
            print(reverseTraversalNode.data)
            reverseTraversalNode = reverseTraversalNode.previous



llist = LinkedList()

nodeOne = Node(10)
nodeTwo = Node(20)
nodeThree = Node(30)

llist.insertEnd(nodeOne)
llist.insertEnd(nodeTwo)
llist.insertEnd(nodeThree)
# llist.deleteHead()

# llist.deleteEnd()

# llist.deleteAt(-90)

llist.printList()