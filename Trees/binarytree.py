class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


# Create root

root = Node(1)

# The 2 and 3 are left & right child of the root note 1.
root.left = Node(2)
root.right = Node(3)

# The 4 is the left child of parent 2.
root.left.left = Node(4)


#############################

'''4 becomes left child of 2
           1
       /       \
      2          3
    /   \       /  \
   4    None  None  None
  /  \
None None'''



