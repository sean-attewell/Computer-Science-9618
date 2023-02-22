# Next, we look at the Fibonacci Sequence.
# This is a series of numbers that starts with 0, 1
# We can derive the next number in the sequence by summing the previous two numbers

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# We can derive the next number in the sequence by summing the previous two numbers — so the following number in the series shown above would be 55 (34 + 21).

# So you can describe any term in the sequence as:

# x_n = x_{n-1} + x_{n-2}

# Using this rule, if you wanted to find the 10th term (zero based counting), you could write:

# x_{10} = x_{10-1} + x_{10-2}
# x_{10} = x_9 + x_8
# x_{10} = 34 + 21
# x_{10} = 55

# Why must this recursion example be some random mathematical oddity???
# It just happens to fit the rules nicely, so is a commonly used example.

# How can we calculate the nth term?
# Let us think of the rules...

# Rule 1
# What is the base case rule?
# The base cases are the first two terms in the sequence, which are just set as 0 and 1
# If you wanted to find the 0th term, well that's is 0, so you can return the argument it was called with
# Likewise if it was called to find the 1st term, just return the 1 it was called with

# Rule 2 + 3
# Must change its state to move towards the base case + call itself
# For every other term, we find the value by summing the previous two terms.
# And we can find the two previous terms with two calls to itself
# This reduces n toward the base case along the way

# Once again finding its solution involved solving the same subproblem multiple times

# Calculate the nth term (zero based counting)
def recursive_fib(n):
    if n <= 1:
        return n
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)

print(recursive_fib(10))
# 55

# To python tutor!
# 710 steps... sheesh.
# Perhaps a good example of terse and elegant
# But not very efficient

# Lets try calling it with a smaller argument to visualise better
# Call it with n = 4. The 4th term should be 3
# 'only' 38 steps

# Even with the use of pythontutor, I think it is hard to follow along mentally
# Give it a go!
# It can be done with some effort, but...
# The issue is that python tutor points to one line at a time
# But our return line does 4 different things on one line:
# Calls itself recusively twice, adds what the calls return together, and then returns that
# ...and we have to remember in our heads which part of the line is running each time it goes back there!

# Let's make this easier for human beings to follow!
# To more clearly illustrate the building of the stack, we will split our return statement up like this

def recursive_fib2(n):
    if n <= 1:
        return n
    else:
        n_minus_1 = recursive_fib2(n-1)
        n_minus_2 = recursive_fib2(n-2)
        return n_minus_1 + n_minus_2

print(recursive_fib2(4))

# Pythontutor tells you what each of the variables are set to
# Before we just didn't have any variable names (aside from the parameter n)
# so what was going on was hidden from us
# Now try to visualise on Pythontutor to the call stack
# Hopefully that's a bit clearer!

# Each call to recursive_fib2 has to recursively call itself until it gets the answer for n_minus_1 
# Then has to recursively call itself to get the answer for n_minus_2 in its execution context
# Then it adds them up
# Which either is the final answer
# Or returned to the call below it on the stack as the answer for n_minus_1 or n_minus_2

# What is the secutiry vulnerability here??
# if we called it with a negative number...