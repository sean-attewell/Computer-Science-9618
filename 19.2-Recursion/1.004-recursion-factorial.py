# Let's look at another typical example used when learning recursion – computing factorials.

# What is a factorial?
# the product of an integer and all the integers below it
# e.g. factorial four (4!) is equal to 24
# 4! = 4 * 3 * 2 * 1 = 24

# Lets make factorials fun
# 52! is the number of different ways you can arrange a single deck of cards. 
# Randomly select one of the 52 cards to be in position 1. 
# Next, randomly select one of the remaining 51 cards for position 2
# then one of the remaining 50 for position 3, and so on... 
# Hence, the total number of ways you could arrange the cards is 52 * 51 * 50 * ... * 3 * 2 * 1, or 52!. 
# Here's what that looks like:
# 80658175170943878571660636856403766975289505440883277824000000000000 

# How big is this number?
# If you shuffle a deck of cards
# You produce a deck which has never been seen in the history of our planet. 
# Never in history has a deck of cards been in that order.
# Yup.

# If every star in our galaxy each had a trillion planets
# Each with a trillion people on them
# and each of these people had a trillion packs of cards
# and each person somehow shuffled all these packs a thousand times a second
# And they'd been doing that since the big bang
# They'd only just now be starting to repeat shuffles

# Ask yourself how many times has anyone inadvertently shuffled the deck to the original order?
# More distraction: https://czep.net/weblog/52cards.html
# but let's get back to the task at hand
# ...Making a recursive algorithm to compute factorials

# Rule 1
# What is the base case rule?
# 4! = 4 * 3 * 2 * 1
# Stop when we hit 1

# Rule 2
# Must change its state to move towards the base case
# we make each subsequent call to factorial on a smaller n

# Rule 3
# Must call itself
# As I mentioned, rule 2 and 3 are usually combined in implementation
# Here we are going to take 1 off the number each time as it calls itself

# As with breaking down the 'sum list' example before...
# For any n! we can solve it by breaking it into smaller sub-problems that also require factorial
# 4 * 3 * 2 * 1
# 4 * (3 * 2 * 1)
# 4 * (3 * (2 * 1))
# 4 * (3 * (2 * (1)))

# You can only multiply two numbers at a time
# We will build up the call stack until we're calling with 1 (which should return 1)
# The multiply it by the prior number each time it unwinds

def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

print(recursive_factorial(5))
# 120

# Viualise on python tutor again

# Whereas in the 'sum list' example we were reducing the length of the list by 1 each time
# Here we just need to reduce the number by 1 each time

# What is the secutiry vulnerability here??
# if we called it with a negative number...


# When does computing factorials come in handy? 
# They are required when figuring combinations; how many ways can we arrange this many items? 
# Or how many orders can there be with this list? 
# Also, they are useful for determining ways of choosing a certain number of items from a collection. 
# For example, if you have 100 different menu items, how many possible 5-item orders could you make?

# So, what clues or hints might you find within a problem that could lead you to use recursion?

# Compute the nth term
# List the first or last n terms
# Generate all permutations

# Another way to think about it is to use the three rules... 
# Is there a clear base case or stopping point that you are working towards (Rule 1)? 
# Is there a straightforward way that the state of the data changes with each iteration that brings it closer to the base case (Rule 2)?