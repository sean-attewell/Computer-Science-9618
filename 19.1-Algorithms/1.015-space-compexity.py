# Space complexity consideres how the memory space required to run an algorithm grows in relation to the input size (number of elements). 
# So it's the same graph, but the y axis is now space requirement rather than number of operations
# It uses the same big O notation

# The algorithm’s speed cannot cause a program’s failure. The speed will rely on the computing power of the machine on which it’s executed. 
# In a worst-case scenario, low computing power will force the algorithm to slow down.
# On the other hand, if an algorithm requires more memory than the machine provides, it won’t complete. 
# Most often, it will cause some type of memory-related error.

# Often, it isn't easy to optimize for time and space at the same time. 
# For instance, by increasing time efficiency, you may need to use more memory and decrease space complexity.


def print_something_a_certain_number_of_times(thing_to_print, number_of_times):
    for _ in range(number_of_times):
        print(thing_to_print)

print_something_a_certain_number_of_times("Get it", 4)

# The function above has a constant O(1) space complexity because no matter how large n gets, the amount of memory being used stays the same.


def append_to_list_a_certain_number_of_times(number_of_times):
    # create an empty list
    my_list = []

    # append to the list the number of times specified by the caller
    for _ in range(number_of_times):
        my_list.append("Shortfin mako shark")

    return my_list

print(append_to_list_a_certain_number_of_times(4))

# This function takes O(n) space
# The space requirement grows in a 1 to 1 relationship with the increase in input size


# We are referring to additional space when we talk about space complexity – meaning that we do not include the memory used by the inputs.
# This function takes constant space (O(1)) even though the input has n items:

def get_the_max(items_list):
    # sets the maximum to negative infinity, so anything else will become the max
    maximum = float("-inf")
    for item in items_list:
        if item > maximum:
            maximum = item

    return maximum

my_list = [9, 3, 4, 4, 2, 98, 23, 4]

print(get_the_max(my_list))
# 98

# As with time complexity it gives the worst-case scenario of an algorithm’s growth rate. 
# We can say that: "the amount of space this algorithm takes will grow no more quickly than this"

# O(1) – constant complexity – takes the same amount of space regardless of the input size
# O(log n) – logarithmic complexity – takes space proportional to the log of the input size
# O(n) – linear complexity – takes space directly proportional to the input size
# O(n log n) – log-linear/quasilinear complexity – also called “linearithmic”, its space complexity grows proportionally to the input size and a logarithmic factor
# O(n^2) – square/polynomial complexity – space complexity grows proportionally to the square of the input size

# Unfortunately, in algorithmics, space and time are like two separate poles. 
# Increasing speed will most often lead to increased memory consumption and vice-versa.

# On the one side, we have merge sort, which is extremely fast but requires a lot of memory. 
# On the other side, we have bubble sort, a slow algorithm but one that occupies minimal space.


# linear search, binary search, bubble sort and insertion sort have space complexity O(1)

# Space Complexity - The amount of extra space used/allocated while running the program determines the space complexity. 

# Linear Search when done sequentially requires us to read all the elements in the array one by one and compare it with the required result. 
# Since we don’t require any extra space, except the iterator, we can say that we require constant extra space for linear search, 
# i.e irrespective of the size of an array, we require the same memory.

# Thus, this is O(1) space complexity.



# ***************************************************************
# BONUS
# ***************************************************************

# Omega Notation – Ω
# Omega notation expresses an asymptotic lower bound.

# So, it gives the best-case scenario of an algorithm’s complexity, opposite to big-O notation. 
# We can say that: “the amount of space this algorithm takes will grow no more slowly than this fix), but it could grow more quickly.”

# Theta Notation – θ
# Theta notation represents a function that is within lower and upper bounds.

# We can say that: “the algorithm’s space takes at least that (lower bound function) amount of space and no more than that (maximum bound function) amount of space”.


# A great example of optimizing the time complexity of the algorithm at the expense of memory is memoization. 
# It’s a technique used to reduce time complexity of algorithms that frequently call some method with the same input data. 
# Instead of calling the method every time, which might be time-consuming, we store the results, and on each call, 
# we check if there is already a cached result for a given input.

# In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again

