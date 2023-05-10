
# Strengths of a Linked List

# The primary strength of a linked list is that operations on the end(s) of the linked list are fast
# (the far end only if you also have a pointer to the tail as well as the head)
# Because it has a reference, doing anything on the end(s) is a constant time operation (O(1)) no matter how many items are stored in the linked list. 

# You also don't have to set a capacity to a linked list when you instantiate it. 
# If you don't know the size of the data you are storing, or if the amount of data is likely to fluctuate, linked lists can work well. 


# Weaknesses of a Linked List

# The main weakness of a linked list is not efficiently accessing an "index" in the middle of the list. 
# The only way that the linked list can get to the seventh item in the linked list is by going to the head node and then traversing one node at a time 
# until you arrive at the seventh node. 
# You can't do simple math and jump from the first item to the seventh.


# What data structures are built on linked lists?

# Remember that linked lists have efficient operations on the end(s) (head and potentially tail). 
# There are two structures that only operate on the ends; queues and stacks. 
# So, most queue or stack implementations use a linked list as their underlying data structure.



# ***************************************************************
# BONUS
# ***************************************************************

# Static arrays have their size or length determined when the array is created and/or allocated
# Python does not have a static array data type. 
# However, lists are built on dynamic arrays. As you will see, dynamic arrays rely on an underlying static array to work.

# Underneath the hood of a dynamic array is a static array. 
# When you create a dynamic array, it is a static array that keeps track of the starting index, the index of the last item that it stores, 
# and the index for the last slot in its capacity. This brings up an important point. 
# An array has a size and a capacity. An array's size is how many items it is storing at the moment. 
# Its capacity is how many items it could store before it runs out of room.

# So, let's say that your dynamic array instantiates with an underlying static array with a capacity of 10 and a size of 0 when you create it. 
# Then, you add ten items to the array. Now, it has a capacity of 10 and a size of 10. 
# If you now go to append an 11th item to the array, you've run out of capacity. Here is where the dynamic of the dynamic array comes into play. 
# The data structure will create a new underlying static array with a capacity twice the size of the original underlying static array. 
# It will then copy the ten original items into the new array and finally add the 11th item. 
# The cost of copying the original items into the new array is O(n). 
# So, when we say that, in the worst-case, an append on a dynamic array has a time-complexity of O(n), this is why. 
# However, all the other appends still have a time-complexity of O(1). So, in the average case append, the time-complexity is still efficient.
# Also, consider that as the array's capacity keeps doubling, the doublings will occur less and less frequently.

# Why is a linked list different than an array? What problem does it solve?

# We can see the difference between how a linked list and an array are stored in memory, but why is this important? 
# Once you see the problem with the way arrays are stored in memory, the benefits of a linked list become clearer.

# The primary problem with arrays is that they hold data contiguously in memory. 
# See contiguous.jpg
# Remember that having the data stored contiguously is the feature that gives them quick lookups. 
# If I know where the first item is stored, I can use simple math to figure out where the fifth item is stored. 
# The reason that this is a problem is that it means that when you create an array, you either have to know how much space in memory you need to set aside
# or you have to set aside a bunch of extra memory that you might not need, just in case you do need it. 

# In other words, you can be space-efficient by only setting aside the memory you need at the moment. 
# But, in doing that, you are setting yourself up for low time efficiency if you run out of room and need to copy all of your elements to a newer, bigger array.
# This is often called a 'doubling append', because your attempt to append data to a full array causes everything to be copied over
# to a new array which has double the space
# Instead of constant time complexity, appending an element to an array becomes linear in this case. 

# Prepending to a Singly linked list, and prepending/appending to a DLL however, will always be constant time

# With a linked list, the elements are not stored side-by-side in memory. Each element can be stored anywhere in memory.
# In addition to storing the data for that element, each element also stores a pointer to the memory location of the next element in the list. 
# The elements in a linked list do not have an index. 
# To get to a specific element in a linked list, you have to start at the head of the linked list and work your way through the list, one element at a time
# to reach the specific element you are searching for. 
# Now you can see how a linked list solves some of the problems that the array data structure has.

# One benefit over a dynamic array is that you don't have doubling appends. 
# This is because each item doesn't have to be stored contiguously; whenever you add an item, you need to find an open spot in memory to hold the next node.