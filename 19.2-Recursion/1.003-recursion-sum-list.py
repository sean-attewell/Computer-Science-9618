# Recursion is ultimately just another way to solve problems. 
# It means breaking down a problem into smaller and smaller sub-problems until the sub-problem is easy to solve.

# Can you write a function to sum the numbers in a list?
# Here is how we would do this without recursion:

def sum_list(items):
    sum = 0
    for i in items:
        sum = sum + i
    return sum

# This iterative function depends on the ability to loop through each item in the list. 
# But another way to iterate through a collection is with recursion.

# How many numbers can you sum without having to rely on the loop construct? 
# The answer is two. 
# But even the loop only sums two at a time.
# How can we think of our problem as a collection of sums of only two numbers?

# separate the problem into two subproblems
# continue doing so until we can no longer divide the problem into two subproblems:
# 1 + 2 + 3 + 4 + 5
# (1 + (2 + 3 + 4 + 5))
# (1 + (2 + (3 + 4 + 5)))
# (1 + (2 + (3 + (4 + 5))))
# (1 + (2 + (3 + (4 + (5)))))

# Once we no longer have a list of items longer than one, we cannot break the list into the first item and the rest of the items. 
# So if someone asks us to sum one number, we know that the result is equal to that number. 
# This "running out" is the base case for our recursive function.

# NOTE: We usually place the base case of a recursive function in the first few lines of the function, though it doesn't have to be there.

# A problem has overlapping subproblems if finding its solution involves solving the same subproblem multiple times.

# OK, let us build. 
# Once again, the three rules for a recursive function are:

# Must have a base case
# Must change its state to move towards the base case
# Must call itself

my_list = [1,2,3,4,5,6]

def sum_list_recursively(items):
    if len(items) == 1: # Base case
        return items[0]
    else:
        return items[0] + sum_list_recursively(items[1:]) # items[1:] has one less item (drops the item at index 0)

print(sum_list_recursively(my_list)) 
# 21

# What is a base case? It allows the algorithm to stop recursing. 
# With our sum_list function, what allows the algorithm to stop recursing?
# It's the first line: if len(items) == 1:
# Notice how if this condition is true, it returns a value and doesn't make a recursive call to itself. 
# We are saying to stop recursing if the list to sum has only one item.

# The second rule is that the algorithm must change its state to move towards the base case.
# How does our function do that? With each subsequent recursion, the list passed into sum_list is one item smaller. 
# For example, on the first recursion, items is [2,3,4,5], and on the subsequent recursion, items is [3,4,5].

# The third rule is that the algorithm must call itself. We are doing this on the final line of the function.
# return items[0] + sum_list(items[1:])

# You can see by visualising on https://pythontutor.com/ that it adds calls until it returns 6 on it's own (the base case)
# Then in the else clause, items[0] was last 5, so you add 6 to it
# Then in the else clause, items[0] was 4 before that, so you add the 11 you just returned to that
# and so on until you return to the original call (piece of paper) at the bottom where items[0] was 1, and you add the 20 you returned

# You can see how the recursive calls go "out" before the stack unwinds, when they starting working their way "back" to the original call.
# The building of the call stack mimics how we visualised it before:
# 1 + 2 + 3 + 4 + 5
# (1 + (2 + 3 + 4 + 5))
# (1 + (2 + (3 + 4 + 5)))
# (1 + (2 + (3 + (4 + 5))))
# (1 + (2 + (3 + (4 + (5)))))

# The innermost bracket at any point represents the current function being called
# It then unwinds from the innermost brackets

