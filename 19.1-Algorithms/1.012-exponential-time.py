# O(2^n) - Exponential Time 

# As the number of elements (n) increases
# The number of operations will grow extremely fast
# Remember that this is inverse case of log growth

# before we looked at base 10 exponentials:
# 10^0 = 1
# 10^1 = 10
# 10^2 = 100
# 10^3 = 1000
# ...
# 10^6 = 1_000_000

# In each step we are only increasing the input by 1, but the output increases by a factor of 10!
# ... because the base is 10, you're multiplying by another 10 each time you increase the exponent by 1

# Here with base 2 exponentials:
# 2^0 = 1
# 2^1 = 2
# 2^2 = 4
# 2^3 = 8
# ...
# 2^6 = 64

# In each step we are only increasing the input by 1, but the output (number of operations) doubles!
# ... because the base is 2, you're multiplying by another 2 each time you increase the exponent by 1
# An algorithm is said to have an exponential time complexity when the growth doubles with each addition to the input data set
# Not as quick as base 10, but still and extremely fast growth in output relative to the growth in input size
# Something you'd want to avoid at all costs

# An example of an exponential time complexity algorithm is the recursive calculation of Fibonacci numbers:

# Calculate the nth term (zero based counting)
def recursive_fib(n):
    if n <= 1:
        return n
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)

print(recursive_fib(10))
# 55

# https://stackoverflow.com/questions/360748/computational-complexity-of-fibonacci-sequence/360773#360773

# Recursive algorithm's time complexity can be estimated by drawing recursion tree
# In this case the recurrence relation for drawing recursion tree would be T(n)=T(n-1)+T(n-2)+O(1) 
# note that each step takes O(1) meaning constant time, since it does only one comparison to check value of n in if block.

# Here lets say each level of above tree is denoted by i hence,

# i
# 0                        n
# 1            (n-1)                 (n-2)
# 2        (n-2)    (n-3)      (n-3)     (n-4)
# 3   (n-3)(n-4) (n-4)(n-5) (n-4)(n-5) (n-5)(n-6)

# You can see the doubling pattern emerge

# What does 2^n mean?
# It means that each time you increase the exponent n by 1, the number of operations doubles
# Because it's base 2, you're multiplying it by another 2!

# How much it can double? ~n times (till n "done") 
# thus you multiply total calls each level in the tree 2*2*2*2... N times which is O(2^n)


# lets say at particular value of i, the tree ends, that case would be when n-i=1, 
# hence i=n-1, meaning that the height of the tree is n-1. 
# Now lets see how much work is done for each of n layers in tree.

# 2^0=1                        n
# 2^1=2            (n-1)                 (n-2)
# 2^2=4        (n-2)    (n-3)      (n-3)     (n-4)
# 2^3=8   (n-3)(n-4) (n-4)(n-5) (n-4)(n-5) (n-5)(n-6)    ..so on
# 2^i for ith level

# Hence total work done will sum of work done at each level, hence it will be 2^0+2^1+2^2+2^3...+2^(n-1) since i=n-1. 
# By geometric series this sum is 2^n, Hence total time complexity here is O(2^n)

# Mathematical approach found here if you need it:
# https://www.youtube.com/watch?v=pqivnzmSbq4