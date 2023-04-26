# Let's look at a code snippet and classify its runtime complexity using Big O notation.

def foo(n):
    i = 1
    while i < n:
        print(i)
        i *= 2

# First, let's think about what the above function is doing. 
# It's printing i… but i is not being incremented by 1, as we usually see. 
# It's doubled every time we run the loop. 
# So, for example, if n = 100, then the final result would be…

# 1
# 2
# 4
# 8
# 16
# 32
# 64

# Or if n = 10, then we would print…

# 1
# 2
# 4
# 8

# We can use the process of elimination to narrow down which runtime classification makes sense for this algorithm. 

# The number of times the loop runs seems to vary based on the value of n, so this is NOT O(1).

# From the above examples, we can also see that the number of times the loop runs is increasing slower than the input size is increasing. 
# n must be doubled before the loop will run one more time. 
# We can eliminate classifications that increase faster than linear time such as O(n log n), O(n^2), O(c^n), and O(n!).

# The only two options left at this point are logarithmic and linear. 
# Since the two growth rates (input, the number of operations) are not the same, this function must run in logarithmic time!