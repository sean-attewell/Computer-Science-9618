# Lists are used to store multiple items in a single variable.
# Python lists are called 'Arrays' in many other languages, so you may hear them referred to as arrays
# Lists are one of 4 built-in data types in Python used to store collections of data
# The other 3 are Tuple, Set, and Dictionary.
# Lists are created using square brackets

# Making an empty list
emptyList = []
print(emptyList)

myList = ["apple", "banana", "cherry"]
print(myList)

# Items in a list are separated with commas, the same way arguments in a function call are.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# This is called zero based indexing

# Imagine a long hallway of rooms, starting with room room 0
# Room 0 contains "apple", room 1 contains "banana" , room 2 contains "cherry"
# Perhaps you can remember the hallway analogy by imagining someone unrolling a really long list down a hallway??
# To access a 'room', knock on the 'door' e.g. myList[]
# Put the number on the door so it knows which door you're knocking e.g. myList[1]

print(myList[0]) # apple
print(myList[1]) # banana
print(myList[2]) # cherry

# You can knock on the door to put something new inside the room!

myList[1] = "tiny kitten"
print(myList) # ['apple', 'tiny kitten', 'cherry']

# The hallway analogy starts to fall apart here...
# But there is also negative indexing
# Like a secret number for each door if you're starting at the end of the hall and working backwards
# -1 refers to the last item, -2 refers to the second last item etc.

print(myList[-1]) # Cherry


# There is an inbuilt function called len(), which works on multiple objects, including lists
print(len(myList)) #3

"""
You can 'slice' both lists and strings
This makes it easy to reference only a portion of a list or string. 

Easiest to explain visualy if you refer to the list-slicing.jpg picture in this folder!

This Stack Overflow answer provides a brief but thorough
overview (but don't worry about the slice object): 
https://stackoverflow.com/a/509295

a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

a[start:stop:step] # start through not past stop, by step

"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[1])

# Output the second-to-last element: 9
print(a[-2])

# Output the last three elements in the array: [7, 9, 6]
print(a[3:])

# Output the two middle elements in the array: [1, 7]
print(a[2:4])

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:5])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[7:12])


# List items are ordered, changeable, and allow duplicate values.

# You can store different data types in a list:

list2 = ["abc", "abc", "abc", 32, True, 40]
print(list2)


# Python has a set of built-in methods that you can use on lists.
# We will cover methods properly later
# We've seen inbuilt functions like print(), and we can make user defined functions
# but methods are essentially a function an object has available, which you access with a '.'


list2.append("anotha one")
print(list2) # ['abc', 'abc', 'abc', 32, True, 40, 'anotha one']

# append()	Adds an element at the end of the list
# pop()	Removes the last element, or the one at the specified position if you give it an arguemnt
# remove()	Removes the item with the specified value
# insert()	Adds an element at the specified position
# extend()	Add the elements of a list (or any iterable -e.g. a string), to the end of the current list
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# index()	Returns the index of the first element with the specified value

# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print(x)


# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)
print(x)

# Extend y with the string "thisstring" (a string is iterable like a list)
y.extend("thisstring")
print(y)

# Iterable is an object which can be looped over or iterated over with the help of a for loop. 
# Objects like lists, tuples, sets, dictionaries, strings, etc. are called iterables. 
# In short and simpler terms, iterable is anything that you can loop over.


# Why would you want to use copy() instead of just assigning one variable to a new variable?

OriginalListToBeDuplicated = [1, 2, 3]

assigned = OriginalListToBeDuplicated
copied = OriginalListToBeDuplicated.copy()

print('OriginalListToBeDuplicated:', OriginalListToBeDuplicated, "Identity:", id(OriginalListToBeDuplicated))
print('assigned:', assigned, "Identity:", id(assigned))
print('copied:', copied, "Identity:", id(copied))

# The copied list has a new identitity (place in memory), so changes to it won't impact the original!

copied.append("I've been changed!")

print("copied:", copied) 
print("OriginalListToBeDuplicated:", OriginalListToBeDuplicated) 

# But if we change the assigned variable...
assigned.append("I've been changed!")
print("assigned:", assigned)
print("OriginalListToBeDuplicated:", OriginalListToBeDuplicated)

# Oops! This changes both 'assigned' and 'OriginalListToBeDuplicated' 
# This is because they both point to the same place in memory!



# ***************************************************************
# BONUS
# ***************************************************************

# There is also a list() constructor just so you're aware, but don't worry too much about this one

listConstructorList = list(("from", "list", "constructor")) # note the double round-brackets

print(listConstructorList) # ['from', 'list', 'constructor']


