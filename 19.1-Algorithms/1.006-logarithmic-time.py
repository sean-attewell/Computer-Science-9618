# O(log n) - Logarithmic Time.	
# This is often refered to simply as 'log time'.

# When an algorithm has O(log n) running time, it means that as the input size grows, the number of operations grows very slowly.
# On the chart you can see that logarithmic growth is barely distinguishable from constant time it grows so slowly!
# Remember our zero counting example in base 10...
# The log wants to be the exponent, and the exponent grows very slowly relative to the growth in input size

# So how does the number of operations grow so slowly in our code?
# An algorithm is said to have a logarithmic time complexity when it reduces the size of the input data in each step
# It doesn’t need to look at all values of the input data!
# Algorithms with logarithmic time complexity are commonly found in operations on binary trees or when using binary search...

# an algorithm that must access all elements of its input data cannot take logarithmic time, 
# as the time taken for reading input of size n is of the order of n.
# But in log time we are reducing the number of elements left in each step.

# Let us re-visit binary search.
# Can you write it from memory? You may need to!

# HINTS
# Steps of the binary search:
# Calculate the middle of the list.
# If the search value is equal to the value in the middle of the list, return the middle (the index).
# If the searched value is lower than the value in the middle of the list, set a new right bounder.
# If the searched value is higher than the value in the middle of the list, set a new left bounder.
# Repeat the steps above until the value is found or the left bounder is equal or higher the right bounder (value not found).

def binary_search(list, item):
  low = 0
  high = len(list) - 1

  while low <= high:
    mid = (low + high) // 2 
    guess = list[mid]

    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1

  return None

mySortedList = [3, 9, 10, 11, 12, 13, 14, 17, 18, 19]

print(binary_search(mySortedList, 11))

# Here is a great visualisation:
# https://www.youtube.com/watch?v=E6IOrZUpvSE

# The end of this video shows the array in a binary tree
# Which is another way to visualise what is going on in binary search
# https://www.youtube.com/watch?v=fDKIpRe8GW4

# So we repeatedly halve the number of elements we are looking at each time.
# How powerful is this?
# If you had 4 billion elements, a linear search could take up to 4 billion guesses in the worst case.
# A binary search for 4 billion (sorted) elements would take at most... 32 guesses!
# This is the power of O(log n) time complexity

# A list with 100 elements might be 15x quicker to check with binary search compared with linear search
# But if the list had 1 billion items, binary search would be more like 33 million times faster!
# As the input size grows, the effect becomes more and more impactful
# This is why we care about big O notation


# ***************************************************************
# BONUS
# ***************************************************************

# If you wanted to 'draw' 16 boxes on a piece of paper by folding the paper
# You 'draw' twice as many boxes with each fold
# You can make 16 boxes with only 4 folds

# This takes O(log n) time!
