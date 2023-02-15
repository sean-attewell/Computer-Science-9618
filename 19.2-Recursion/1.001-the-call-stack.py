# Call stack helps us understand recursion.

# A stack is:

# Linear
# Ordered
# Data is accessed from only one end

# See push-pop.jpg

# Think of a stack of books, one piled on top of the other
# You can 'push' a new book onto the top of a stack 
# or 'pop' a book off the top

# This is much like the list method list.pop()
# Though instead of push, lists call it list.append() - but it's the same thing
# Unlike a list, a stack is ONLY accessed in a last-in first-out order (LIFO)
# You can only access the top of the stack - which is the last one added

# But what is the *CALL* stack?
# A stack to maintain a record of the subroutine (think method, or function) currently being run 
# and where it should return to once it has’s finished executing
# So the top of the stack is the subroutine currently being run
# and once that is done, it 'pops' off the stack
# it returns to the subroutine below it in the stack

# Each function, its parameters, and variables are pushed into the call stack to form a stack frame (execution context). 
# The stack frame is simply the memory location. 
# If a function calls another, the stack grows by a frame. 
# As functions return (finish) they are removed from the stack (and the memory they had occupied is cleared).

# If the stack takes up more space than it had assigned to it, it results in a “stack overflow” error

# For the love of god give me a real example!
# OK, we have two functions defined in our scope — one to add 2 to our input, and another to add 4.

def add_two(num):
    return num + 2

def add_four(num):
    return add_two(add_two(num))

# NOTE: the above example is not recursion... 
# add_two doesn't call itself when we define it
# When we define add_four we just call add_two twice...
# The first time to return what we will use as the argument the second time it is called...
# It's not actually calling itself
# Not confusing at all.

# Let's think about what the call stack looks like when we call these functions. First, what happens when we run the following:

add_two(2)

# add_two call gets pushed onto the call stack
# num gets stored in memory with the value 2
# num + 2 gets returned as 4 and that call gets popped off
# There are no more functions below in the call stack to execute, so we're done

add_four(6)

# add_four call gets pushed on the stack, and 6 gets stored as num
# the innermost add_two call gets pushed onto the stack, and 6 gets stored as num
# the innermost add_two call returns 8 and pops off
# the second add_two call gets pushed onto the stack with 8 as num
# the second add_two call returns 10 and gets popped off
# we are back in the context of add_four, which now returns 10 and pops off the stack
# the stack is now empty

# You may find it useful to visualise the execution step by step on this website:
# https://pythontutor.com/visualize.html#mode=edit
# (imagine it shows the stack on the right hand side upside down)

# Can you explain the call stack in the below code?

def add_ten(num):
    return add_two(add_four(add_four(num)))

print(add_ten(5))