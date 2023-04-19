# What are we supposed to do with the constants?

def do_a_bunch_of_stuff(list_of_things):  # O(1 + n/2 + 1000)
    last_idx = len(list_of_things) - 1
    print(list_of_things[last_idx])  # O(1)

    middle_idx = len(list_of_things) / 2
    idx = 0
    while idx < middle_idx:  # O(n/2)
        print(list_of_things[idx])
        idx = idx + 1

    for num in range(1000):  # O(1000)
        print(num)

my_list = ['thing 1', 'thing 2', 'thing 3', 'thing 4', 'thing 5']
do_a_bunch_of_stuff(my_list)

# print(items[last_idx]) is constant time because it doesn't change as the input changes. So, that portion of the function is O(1).

# The while loop that prints up to the middle index is 1/2 of whatever the input size is; we can say that portion of the function is O(n/2).

# The final portion will run 1000 times, no matter the size of the input.

# So, putting it all together, we could say that the efficiency is O(1 + n/2 + 1000). 
# However, we don't say this. 
# We describe this function as having linear time O(n) because we drop all of the constants. 
# Why do we cut all of the constants? Because as the input size gets huge, adding 1000 or dividing by 2 has minimal effect on the algorithm's performance.


# Do constants ever matter?

# Complexity analysis with Big O notation is a valuable tool. 
# It would be best if you got in the habit of thinking about the efficiency of the algorithms you write and use in your code. 
# However, just because two algorithms have the same Big O notation doesn't mean they are equal.

# Imagine you have a script that takes 1 hour to run. 
# By improving the function, you can divide that runtime by six, and now it only takes 10 minutes to run. 
# With Big O notation, O(n) and O(n/6) can both be written as O(n), 
# but that doesn't mean it isn't worth optimizing the script to save 50 minutes every time the script runs!

# It is your job as a developer to know when making your code more efficient is necessary. 
# You will always be making calculated tradeoffs between runtime, memory, development time, readability, and maintainability. 
# It takes time to develop the wisdom to strike the right balance depending on the scenario.

# No right answers, only trade offs
# Definitely some wrong answers though.





# Let's look at a few code snippets and classify their runtime complexity using Big O notation.

def foo(n):
    i = 1
    while i < n:
        print(i)
        i *= 2

# First, let's think about what the above function is doing. 
# It's printing i…but i is not being incremented by 1, as we usually see. 
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
# We can eliminate classifications that increase faster than constant time such as O(n log n), O(n^c), O(c^n), and O(n!).

# The only two options left at this point are logarithmic and linear. 
# Since the two growth rates (input, the number of operations) are not the same, this function must run in logarithmic time!