# If your list is sorted in order, we can do better than linear search:

# If you are looking for a word in the dictionary that begins with K,
# (I'm talking about a physical dictionary book, not the python meaning of dictionary) 
# you wouldn't start at the start and go through one by one like linear search...
# because it's sorted in alphabetical order, we can do better.

# If someone asked you to guess a number between 1 and 100, and could give feedback of 'too high' or 'too low'
# You wouldn't guess 1, then 2, then 3...

# With binary search you guess the middle number, and eliminate half the remaining numbers each time
# Guessing out of a hundred numbers could take 100 steps with linear search
# But only a max of 7 steps with binary search:
# 100 --> 50 --> 25 --> 13 --> 7 --> 4 --> 2 --> 1

# A dictionary with 2400 words...
# Linear search could take 2400 steps
# Binary only 18

# But do remember, binary search only works when your list is in sorted order. 


def binary_search(list, item):
  # low and high indexes keep track of which part of the list you'll search in.
  low = 0
  high = len(list) - 1

  # While you haven't narrowed it down to one element ...
  while low <= high:
    # ... check the middle element
    mid = (low + high) // 2 # round the result down to the nearest whole number
    guess = list[mid]
    # Found the item.
    if guess == item:
      return mid
    # The guess was too high.
    if guess > item:
      high = mid - 1
    # The guess was too low.
    else:
      low = mid + 1

  # Item doesn't exist
  return None

mySortedList = [3, 9, 10, 11, 12, 13, 14, 17, 18, 19]

print(binary_search(mySortedList, 11))
#3


# In general, for any list of n items, binary search will take log2 n steps to run in the worst case
# simple linear search will take n steps.

# Logarithms
# You may not remember what logarithms are, but you probably know what exponentials are. 
# log10 100 is like asking, “How many 10s do we multiply together to get 100?” 
# The answer is 2: 10 × 10. 
# So log10 100 = 2. 
# Logs are the flip of exponentials.

# For binary search, you have to check log2 n elements in the worst case. 
# For a list of 8 elements, log2 8 == 3, because 2^3 == 8. 
# So for a list of 8 numbers, you would have to check 3 numbers at most. 

# For a list of 1,024 elements, log2 1,024 = 10, because 2^10 == 1,024. 
# So for a list of 1,024 numbers, you’d have to check 10 numbers at most.

# Q: What is the maximum number of steps it would take binary search to find a sorted list of 128 numbers?
# A: 7

# Either you can calculate Log2 128 = 7 (i.e. 2^7 = 128)
# or you can see how many times we have to halve 128 with our binary search
# 128 --> 64 --> 32 --> 16 --> 8 --> 4 --> 2 --> 1

# Q: Suppose you double the size of the list - what's the maximum number of steps now?
# Try and work this out intuitively!
# A: 8 

# One more doubling requires one more halving!