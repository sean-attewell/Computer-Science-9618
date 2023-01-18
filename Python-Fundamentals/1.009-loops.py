# You can use two types of loops in Python, a for loop and a while loop. 

# A for loop iterates over a given sequence (iterator expression).
# A while loop repeats as long as a boolean context evaluates to True.

# for loop:

myList = ["apple", "banana", "cherry"]

for fruit in myList:
    print(fruit)

# A list is an iterable
# So you can use a for loop to iterate over it! 
# for and in are keywords
# Note that we have created the fruit variable 
# This changes to a different member of the list each loop

print(fruit) # this now prints cherry as it was the last one it was set to


# The range() inbuilt function returns a sequence of numbers:
# starting from 0 by default
# increments by 1 (by default)
# and stops _before_ a specified number (does this remind of you slicing lists?)

# range(start, stop, step)

# Prints 0, 1, 2, 3, 4
for x in range(5):
    print(x)

# So the inbuilt range function has created an iterable to loop over

# Prints 2, 3, 4, 5, 6
for x in range(2, 7):
    print(x)

# Prints 1, 3, 5, 7
for x in range(1, 8, 2):
    print(x)


# while loop:

# The While loop will keep looping WHILE a boolean evaluates to true.
# Between the while keyword and the colon is a boolean context.
# Just as it was between the if keyword and the colon in conditional statments.

# Prints 0, 1, 2, 3, 4
count = 0
while count < 5:
    print(count)
    count = count + 1

# Have we seen '+=' before?
# += is Addition Assignment operator
# lets you add two values together and assign the resultant value to a variable.
# otherwise you'd have to write: count = count + 1

# Prints 2, 3, 4, 5, 6
count = 2
while count < 7:
    print(count)
    count += 1

# Prints 1, 3, 5, 7
count = 1
while count < 8:
    print(count)
    count += 2


# You can use a break statement to exit a for loop or a while loop.

# Prints 0, 1, 2, 3, 4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# "While True" will always evaluate to true, so it will go on forever
# The break statement terminates the loop containing it. 
# In this example the while loop stops at 4 because it hit the break
# If the break statement is inside a nested loop (loop inside another loop), the break statement will only terminate the innermost loop.


# You can use the continue statement to skip the rest of the code inside a loop for the current iteration only.
# The loop does not terminate entirely but continues with the next iteration.

# Prints 1, 3, 5, 7
for x in range(8):
    if x % 2 == 0:
        continue
    print(x)

# if x is even, skip this block and do not print


# ***************************************************************
# BONUS
# ***************************************************************

# https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/

# If you only need to loop over a single list just use a for-in loop
# If you need to loop over a list and you need item indexes, use enumerate
# If you need to loop over multiple lists at the same time, use zip

# Stackoverflow example Q
# https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops

ints = [8, 23, 45, 12, 78]

# How would you print both the index and the number?

i = 0
for num in ints:
    print(f'item #{i} = {num}')
    i += 1

# Here we manually make a counter to track the indexes we need

# The enumerate function gives us an iterable where each element is a tuple that contains the index of the item and the original item value.

# This function is meant for solving the task of:
# Accessing each item in a list (or another iterable)
# Also getting the index of each item accessed
# So whenever we need item indexes while looping, we should think of enumerate.


ints = [8, 23, 45, 12, 78]

for i, num in enumerate(ints):
    print(f'item #{i} = {num}')

# Generally indexes are for accessing the data at that index
# But we already have access to it in a regular for in loop, so this will be rare.


# The start=1 in the example below is optional. 
# It starts counting at 0 by default (which matches the actual index).

# for i, num in enumerate(ints, start=1):
#     print(f'item #{i} = {num}')




# https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/

# Often when we use list indexes, it’s to look something up in another list.

colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for i, color in enumerate(colors):
    ratio = ratios[i]
    print(f"{ratio * 100}% {color}")

# Note that we only need the index in this scenario because we’re using it to lookup elements at the same index in our second list. 
# What we really want is to loop over two lists simultaneously: the indexes just provide a means to do that.

# We don’t actually care about the index when looping here. Our real goal is to loop over two lists at once. This need is common enough that there’s a special built-in function just for this.

# Python’s zip function allows us to loop over multiple lists at the same time:

colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for color, ratio in zip(colors, ratios):
    print(f"{ratio * 100}% {color}")


# The zip function takes multiple lists and returns an iterable that provides a tuple of the corresponding elements of each list as we loop over it.

# Note that zip with different size lists will stop after the shortest list runs out of items.


# If you find yourself tempted to use range(len(my_list)) or a loop counter, 
# think about whether you can reframe your problem to allow usage of zip or enumerate (or a combination of the two).

# In fact, if you find yourself reaching for enumerate, think about whether you actually need indexes at all. It’s quite rare to need indexes in Python.
