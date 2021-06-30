# Tree Traversal:

# Depth First Traversal:
# 1. Inorder --> (left--root--right)
# 2. preorder --> (root--left--right)
# 3. postorder --> (left--right--root)

# Breath First Traversal
# Level Order Traversal


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order_traversal(self,start,traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.pre_order_traversal(start.left,traversal)
            traversal = self.pre_order_traversal(start.right,traversal)
        return traversal

    def print_tree(self,traversal_type):
        if traversal_type == 'preorder':
            return self.pre_order_traversal(obj1.root,'')
        else:
            print(f'Traversal Type {traversal_type} is not supported.')
            return False




# Tree structure:
'''
           1
       /       \
      2          3
    /   \       /  \
   4     5    6     7 '''

# Inorder   : 4 2 5 1 6 3 7 
# preorder  : 1 2 4 5 3 6 7 
# postorder : 4 5 2 6 7 3 1

# Level order : 1 2 3 4 5 6 7


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
first.left = second
first.right = third 
second.left = fourth
second.right = fifth
third.left = sixth
third.right = seventh

print(obj1.print_tree('preorder'))









