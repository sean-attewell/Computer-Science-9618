# O(n!) - Factorial time.
# As the input size increases, the runtime will grow astronomically, even with relatively small inputs.

# Factorial growth is brutal as we discussed before:

# 2! = 2 x 1 = 2
# 3! = 3 x 2 x 1 = 6
# 4! = 4 x 3 x 2 x 1 = 24
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# 6! = 6 x 5 x 4 x 3 x 2 x 1 = 720
# 7! = 7 x 6 x 5 x 4 x 3 x 2 x 1 = 5040
# 8! = 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 40320

# it almost looks like a straight vertical line on our big O complexity chart 

# A great example of an algorithm which has a factorial time complexity is the Heap’s algorithm,
# which is used for generating all possible permutations of n objects.
# "Heap found a systematic method for choosing at each step a pair of elements to switch, 
# in order to produce every possible permutation of these elements exactly once"

def heap_permutation(data, n):
    if n == 1:
        print(data)
        return
    
    for i in range(n):
        heap_permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n-1] = data[n-1], data[i]
        else:
            data[0], data[n-1] = data[n-1], data[0]


data = [1, 2, 3]
heap_permutation(data, len(data))

# [1, 2, 3]
# [2, 1, 3]
# [3, 1, 2]
# [1, 3, 2]
# [2, 3, 1]
# [3, 2, 1]

# Another great example is the Travelling Salesman Problem
# "Given a list of cities and the distances between each pair of cities, 
# what is the shortest possible route that visits each city exactly once and returns to the origin city?"

# But neither that or Heap's algorithm are on your syllabus


# ***Careful!***
# Just to avoid any confusion, I will note that the recursive factorial algorithm we looked at before
# does NOT have factorial time complexity
# What time complexity do you think it does have?

def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

print(recursive_factorial(5))
# 120

# this algorithm is linear, running in O(n) time. 
# This is the case because it executes once every time it decrements the value n
