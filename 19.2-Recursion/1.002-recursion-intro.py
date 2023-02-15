# Recursive functions call themselves
# Here is a simple recursive function

def print_to_zero(n):
    if n < 0: # base case
        return
    print(n)
    return print_to_zero(n - 1) # recursive case

print_to_zero(5)
# 5
# 4
# 3
# 2
# 1
# 0

# Often, recursive solutions are terse and elegant. 
# But recursive solutions are not always the most efficient

# The base case is a way to return without continuing making recursive calls forever. 
# In other words it is the mechanism that stops this process of ever more recursive calls 
# and an ever growing stack of function calls waiting on the return of other function calls

# What would happen if our base case was n == -1?
# It works fine if used as intended
# But we must do our best to pre-empt adversarial actors
# a == -1 base case could lead to infinite recursion if it was called with a negative number smaller than -1 
# the base case wouldn't hit and it would keep taking away 1

# The < 0 base case causes it to return only when n is reduced to below 0
# BUT it also returns straight away if you try and print something smaller than 0

# Shall we try and break stuff??
# Python will eventually throw the following error
# "RecursionError: maximum recursion depth exceeded while calling a Python object"
# It's a guard against a stack overflow!
# A stack overflow is a runtime error that happens when a program runs out of memory in the call stack

# Lets return to:
# https://pythontutor.com/visualize.html#mode=edit

# Look how it stacks all the way up to n = -1 with calls of the same function
# and then UNWINDS
# As the top of the stack returns, it is popped off
# it returns to where it was in the call below it in the stack

# I think of this as a stack of paper
# you're reading code down the piece of paper
# when you hit a recursive call you pause where you are and stack a new piece of paper on top
# read down that new piece from the top
# if it hits another recursive call, again pause where you are, and add a new piece on top
# When the piece of paper you're reading returns, take it off the stack
# continue at the place you paused on the paper below

# Maybe just delete and try to re-write it for pracise?
# Remember the three rules for a recursive function are:

# Must have a base case
# Must change its state to move towards the base case
# Must call itself

# What happens if we put the infinitely recursive version into pythontutor I wonder...


# Every time we add a new call to the stack, we are increasing the amount of memory that we are using. 
# If we are analyzing the algorithm using Big O notation, then we might note that this increases our space complexity.

# There are times when we might want to pay this cost in order to get a short, useful algorithm, like when we are traversing a tree. 
# But there are other times when there may be better, more efficient ways of solving this problem.
