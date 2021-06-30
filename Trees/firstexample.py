class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)


# Tree structure:
'''
           1
       /       \
      2          3
    /   \       /  \
   4     7     9    10
  /  \
5     6'''


# Set up the tree:

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.right.left = Node(9)
tree.root.right.right = Node(10)
tree.root.left.left = Node(4)
tree.root.left.right = Node(7)
tree.root.left.left.left = Node(5)
tree.root.left.left.right = Node(6)



