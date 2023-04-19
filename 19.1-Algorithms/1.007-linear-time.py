# O(n) - Linear Time. 
# means the number of operations grows at the same rate as the input size. 
# Linear growth.


def print_list(list_of_things):
    for thing in list_of_things:
        print(thing)

my_list = ['thing 1', 'thing 2', 'thing 3', 'thing 4', 'thing 5']

print_list(my_list)


# We saw this when we looked at linear search:

def linear_search(arr, x):
 
  for i in range(len(arr)):
    if arr[i] == x:
      return i
 
  return -1


print(linear_search(my_list, "thing 3"))
# 2

# There is a one to one correlation between the size of the input
# and the number of operations in the worst case

# If you were looking through a dictionary for the word aardvark with linear search
# the fact it might be the first word you find, doesn't mean it's somehow constant time O(1)
# With big O notation, we always care about the WORST case scenario.


# ***************************************************************
# BONUS
# ***************************************************************

# If you wanted to 'draw' 16 boxes on a piece of paper by drawing 16 boxes...
# That's 16 steps to draw 16 boxes

# This takes O(n) time!
