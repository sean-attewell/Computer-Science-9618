# A linked list is a simple, linear data structure used to store a collection of elements. 
# Unlike an array, each element in a linked list does not have to be stored contiguously in memory.

# *Aside about dynamic arrays* (let me know if you need to know!)

# Because the elements are not stored contiguously, each element in memory must contain
# information about location of the next element in the list. 
# the next item in the list could be located anywhere in memory. 
# It could even come before the first item in memory.

# See linked-list.png
# Note that the first item is referred to as the head
# the last item does not point to anything, so just points to null (we will set this to None in python)

# There are no idexes like you have with an array!
# So you can't just jump to an index, you have to traverse through the linked list. 
# Starting with the head you have to see where each node points to one by one to get to the end
# That takes linear time, which is a lot slower

# Pretty much any type of data can be stored in a linked list. 
# Strings, numbers, booleans, and other data structures can be stored. 
# You should not feel limited using a linked list based on what type of data you are trying to store.

# The elements in a linked list can be either sorted or unsorted. 
# There is nothing about the data structure that forces the elements to be sorted or unsorted.

# Linked lists can contain duplicates. 
# There is nothing about the linked list data structure that would prevent duplicates from being stored.

# See linked-list-types.png

# There are three types of linked lists: 
# singly linked list (SLL)
# doubly linked list (DLL)
# circular linked list. 

# All linked lists are made up of nodes where each node stores the data and also information about other nodes in the linked list.

# Each singly linked list node stores the data and a pointer where the next node in the list is located. 
# Because of this, you can only navigate in the forward direction in a singly linked list. 
# To traverse an SLL, you need a reference to the first node called the head. 
# From the head of the list, you can visit all the other nodes using the next pointers.

# Each node in a DLL also stores a reference to the previous item. 
# Because of this, you can navigate forward and backward in the list. 
# A DLL also usually stores a pointer to the last item in the list (called the tail).

# A Circular Linked List links the last node back to the first node in the list. 
# This linkage causes a circular traversal; 
# when you get to the end of the list, the next item will be back at the beginning of the list.

# Lets implement our very own Singly Linked List!

class LinkedListNode:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self, headData=None):  
    self.head = LinkedListNode(headData) # Containment - a linked list has a node

  def append(self, data): # Appending to tail 
    new_node = LinkedListNode(data)

    if self.head:
      current = self.head # Starts at the start, if there is a start

      while current.next: # if the node links to another, go to the next one
        current = current.next

      current.next = new_node # When you get to the end, link it to the new node
    else:
      self.head = new_node # If there is no head, new node becomes the head

  def prepend(self, data):
    newhead = LinkedListNode(data)
    newhead.next = self.head
    self.head = newhead

  def deleteValue(self, valueToDelete):
    if self.head == None:
      return

    if self.head.data == valueToDelete:
      self.head = self.head.next
      return
      
    current = self.head
    while current.next:
      if current.next.data == valueToDelete:
        current.next = current.next.next
        return
      current = current.next
  
  def findIndexOfData(self, valueToFind):

    if self.head == None:
      return -1

    current = self.head
    index = 0
    while current:
      if current.data == valueToFind:
          return index
      current = current.next
      index += 1

    return -1

  def findDataAtIndex(self, indexToFind):
    if self.head == None:
      return -1

    if indexToFind < 0:
      return -1

    currentNode = self.head
    currentIndex = 0
    while currentNode and currentIndex < indexToFind:
      currentNode = currentNode.next
      currentIndex += 1

    if currentNode:
      return currentNode.data
    else:
      return -1

  def insertAtIndex(self, data, insertionIndex):
    new_node = LinkedListNode(data)
    if insertionIndex == 0:
        new_node.next = self.head
        self.head = new_node

    Index = 0
    current = self.head    
    while current:
        if Index + 1 == insertionIndex:
            new_node.next = current.next
            current.next = new_node
            return
        else:
            Index += 1
            current = current.next

  def print(self):
    current = self.head
    while current:
        print(current.data)
        current = current.next

my_ll = LinkedList(1)
my_ll.append(2)
my_ll.append(3)

print(my_ll.head.data) # 1
print(my_ll.head.next) # <__main__.LinkedListNode object at 0x00000221075F3940>

print(my_ll.head.next.data) # 2
print(my_ll.head.next.next.data) # 3

# Note that append adds to the tail rather than pre-pending to the head.
# Hence it has to traverse through the linked list with linear time O(n)
# That's because this is a singly linked list (SLL)
# A doubly linked list (DLL) also usually stores a pointer to the last item in the list (called the tail)
# For a doubly linked list it would therefore be constant time O(1) to append to the end too

# Let's make a prepend method!

my_ll.prepend(0)
my_ll.prepend(-1)
print(my_ll.head.data) # -1
print(my_ll.head.next.data) # 0
print(my_ll.head.next.next.data) # 1

# Insert at the beginning of the linked list is constant time O(1)
# This is called pre-pend, you're putting it before the current head, to give it a new head

# Let's add a print method to make life easy!
print('**************************************')
my_ll.print()

# (Should have really made a repr() function - returns a printable representational string of the given object()

# let's make a method to delete a value

print('**************************************')
my_ll.deleteValue(2)
my_ll.print()

print('**************************************')
# Lets test deleting the head
my_ll.deleteValue(-1)
my_ll.print()

# linear time O(n) as it must go through the list one by one until it finds it
# If we made a 'delete head' method the head only it would be constant time O(1), just like prepend
# These operations at the head of a SLL don't have to traverse anywhere and so are constant time

# Very good explanation of the above (though it's in java not python)
# https://www.youtube.com/watch?v=njTh_OwMljA 


print('**************************************')

# Your syllabus specifies that you should be able to write an algorithm to find an item in a linked list
# Well, let's say we want to know which node the data is located at
# Then we essentially end up giving each node an index
# But since you can't just jump to an index like you can with an array, this isn't particularly useful

print(my_ll.findIndexOfData(22)) # -1
print(my_ll.findIndexOfData(3)) # 2

# Perhaps you could do the same thing but just return true if it exists in the linked list

print('**************************************')

# The other thing you could do is specify an index and search for that data at that index:
my_ll.print()

print("search index -7:", my_ll.findDataAtIndex(-7))
print("search index 0:",my_ll.findDataAtIndex(0))
print("search index 1:",my_ll.findDataAtIndex(1))
print("search index 2:",my_ll.findDataAtIndex(2))
print("search index 3:",my_ll.findDataAtIndex(3))

# To look up an item by index in a linked list is linear time (O(n)). 

print('**************************************')

# https://www.freecodecamp.org/news/introduction-to-linked-lists-in-python/
# Lets say you wanted to insert into a particular index
# (Again this is not a very linked list thing to be doing... just trying to cover all bases)

my_ll.print()
my_ll.insertAtIndex("new head", 0)
my_ll.print()
print('**************************************')
my_ll.insertAtIndex(55, 2)
my_ll.print()
print('**************************************')
my_ll.insertAtIndex(99, 4)
my_ll.print()
print('**************************************')
my_ll.insertAtIndex(101, 6)
my_ll.print()
print('**************************************')
my_ll.insertAtIndex(104, 8)
my_ll.print()