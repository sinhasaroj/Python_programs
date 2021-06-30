class Node:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root=None):
        self.root = None


        


# Tree structure:
'''
           1
       /       \
      2          3
    /   \       /  \
   4     5    6     7 '''


# Set up the tree..

obj1 = BinaryTree()

first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)
seventh = Node(7)

# Connecting the nodes...

obj1.root = first
# print(first.value) ---> 1

first.left = second
# print(first.left.value)  -- 2

first.right = third 
# print(first.right.value)  --> 3

second.left = fourth
second.right = fifth

third.left = sixth
third.right = seventh

# print(first.left.left.value) ---> 4
# print(first.left.right.value) --->5







