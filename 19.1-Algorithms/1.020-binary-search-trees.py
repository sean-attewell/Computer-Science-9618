# A tree is a type of data structure
# A binary tree is a specific type of tree. 

# It is called a binary tree because each node in the tree can only have a maximum of two child nodes. 
# It is common for a node's children to be called either left or right.

# class BinaryTreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# Just like a binary tree is a specific type of tree, a binary search tree (BST) is a specific type of binary tree. 
# A binary search tree is just like a binary tree, except it follows specific rules about how it orders the nodes contained within it. 
# For each node in the BST, all the nodes to the left are smaller, and all the nodes to the right of it are larger.

# Remember when we looked at binary search how the array had to be sorted?
# Imagine resorting the array every time you added a new piece of data
# Imagine if instead you could slot the data into the right slot straight away...
# That's the idea behind the binary search tree data structure

# But remember, you don't get random access like with an array - You can't say "give me the item at the fith index"

# We can call a binary search tree balanced if the heights of its left and right subtrees differ by at most one, 
# and both of the subtrees are also balanced.


# Time and Space Complexity

# Provided it is reasonably balanced:
# The order of nodes in a BST means that each comparison skips about half of the remaining tree
# so the whole lookup takes time proportional to the binary logarithm of the number of items stored in the tree

# Lookup
# If a binary search tree is balanced, then a lookup operation's time complexity is logarithmic (O(log n)). 
# If the tree is unbalanced, the time complexity can be linear (O(n)) in the worst possible case 
# (virtually a linear chain of nodes will have all the nodes on one side of the tree).

# Insert
# If a binary search tree is balanced, then an insertion operation's time complexity is logarithmic (O(log n)). 
# If the tree is entirely unbalanced, then the time complexity is linear (O(n)) in the worst case.

# Delete
# If a binary search tree is balanced, then a deletion operation's time complexity is logarithmic (O(log n)). 
# If the tree is entirely unbalanced, then the time complexity is linear (O(n)) in the worst case.


# Let's look at an implementation:
# To create a binary search tree, we need to define two different classes: 
# one for the nodes that will make up the binary search tree and another for the tree itself

# The first difference to the other data structures we have looked at which you will notice is that
# the node implementation itself contains methods...

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def search(self, target):
        if self.value == target:
            return self
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(target)

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value)
        if self.right:
            self.right.PrintTree()

class BST:
    def __init__(self, value):
        self.root = BSTNode(value)

    def insert(self, value):
        self.root.insert(value)

    def search(self, value):
        return self.root.search(value) # 200 IQ move from Ana

    def PrintTree(self):
      self.root.PrintTree()

my_BST = BST(8)
my_BST.insert(3)
my_BST.insert(10)
my_BST.insert(1)
my_BST.insert(6)
my_BST.insert(14)
my_BST.insert(4)
my_BST.insert(7)
my_BST.insert(13)

my_BST.PrintTree() # prints in size order


print(my_BST.search(99)) # False
print(my_BST.search(10)) # returns node object
print(my_BST.search(4)) # returns node object

# Strengths
# One of the main strengths of a BST is that it is sorted by default
# You can pull out the data in order by using an in-order traversal, as with our print function. 
# BSTs also have efficient average searches, provided they are balanced (O(log n)) 
# Provided they are balanced they have the same efficiency for their searches as a sorted array using binary search

# Weaknesses
# The primary weakness of a BST is that they only have efficient operations if they are balanced. 
# The more unbalanced they are, the worse the efficiency of their operations gets. 
# Another weakness is that they don't have stellar efficiency in any one operation. 
# They have good efficiency for a lot of different operations. So, they are more of a general-purpose data structure.

# If you want to learn more about trees that automatically rearrange their nodes to remain balanced, look into AVL trees or Red-Black trees


# ***************************************************************
# BONUS
# ***************************************************************

# https://www.programiz.com/dsa/binary-tree
# Have a look at different types of binary trees on the above link!

# "Perfect" Trees
# A "perfect" tree has all of its levels full. This means that there are not any missing nodes in each level.
# "Perfect" trees have specific properties: 

# First, the quantity of each level's nodes doubles as you go down.
# Second, the quantity of the last level's nodes is the same as the quantity of all the other nodes plus one.

# The height of a tree is the number of levels that it contains. 
# Based on the properties outlined above, we can deduce that we can calculate the tree's height with the following formula:

# log_2(n+1) = h

# where n is the number of nodes
# so a perfect tree with 15 nodes, the height is 4
# because the exponent of 2 that gives you 16 is 4

# If you know the tree's height and want to calculate the total number of nodes, you can do so with the following formula:

# n = 2^h - 1

# so a perfect tree with a height of 4 has 15 nodes.