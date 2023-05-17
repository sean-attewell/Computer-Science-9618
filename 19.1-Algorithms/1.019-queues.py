# A queue is a data structure that stores its items in a first-in, first-out (FIFO) order. 
# It functions just like a queue (or a line) would in everyday life.

# When are queues useful?
# Queues are useful data structures in any situation where you want to make sure things are processed in a FIFO order. 
# Think of a web server. The server might be trying to service thousands of page requests per minute. 
# It would make the most sense for the server to process and respond to the requests in the same order that they were received. 
# That way, the first client to request a page is the first client to receive a response. 


class LinkedListNode:
  def __init__(self, data):
    self.data = data
    # next points in the direction of the rear of the queue
    self.next = None


class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    # Imagine taking a birds eye view
    # North is the front of the queue, South is the rear
    # Remember next points to the rear (south)

  def enqueue(self, item):
    new_node = LinkedListNode(item)
    # check if queue is empty
    if self.rear is None:
      self.front = new_node
      self.rear = new_node
    else:
      # add new node to rear
      self.rear.next = new_node
      # reassign rear to new node
      self.rear = new_node

  def dequeue(self):
    # check if queue is empty
    if self.front:
      # keep copy of old front to return
      old_front = self.front
      # set new front
      self.front = old_front.next # remember it points in the direction of the rear

    # check if the queue is now empty
    if self.front is None:
      # make sure rear is also None
      self.rear = None

    return old_front

  def print(self):
    current = self.front
    while current:
      print(current.data)
      current = current.next

my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)

my_queue.print()

# To enqueue an item (add an item to the back of the queue) takes O(1) time.

print("************************************")

my_queue.dequeue()

my_queue.print()

print("************************************")

my_queue.dequeue()

my_queue.print()

# To dequeue an item (remove an item from the front of the queue) takes O(1) time.


print("************************************")

my_queue.enqueue(6)
my_queue.enqueue(7)

my_queue.print()


# Another operation you might have is 'Peek'
# To peek at an item (inspect the item from the front of the queue without removing it) takes O(1) time.

# Strengths
# The primary strength of a queue is that all of its operations are fast (take O(1) time).

# Weaknesses
# There are no weaknesses in this data structure. The reason is that it is a very targeted data structure designed to do a few things well.

