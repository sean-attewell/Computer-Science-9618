# When given a choice between different algorithms, we want to choose the most efficient algorithm 

# Big O notation, represents an algorithm's worst-case complexity. 
# It uses algebraic terms to describe the complexity of an algorithm. 

# What do you mean 'complexity'? Are you going to define this??
# Why is it called big O??
# You should be shouting this at your teachers

# Big O notation is called this because:
# "Big" means "capital", as in capital letter
# The letter O was chosen to stand for Ordnung, meaning the order of approximation.

# You may use big O to consider both time complexity and space complexity depending on your needs
# I think efficiency is a better word, but what it really means in computer science is:

# ***Big O notation is used to classify algorithms according to how their run time or space requirements grow as the input size grows***

# We will start by looking at time efficiency
# Big O defines the runtime required to execute an algorithm by identifying how the performance of your algorithm will change as the input size grows
# But it does not tell you how fast your algorithm's runtime is.
# The actual runtime depends on the specific computer running the algorithm, so we cannot compare efficiencies that way. 
# By focusing on the general growth, we can avoid exact runtime differences between machines and environments.

# We talk about runtime relative to the input size because we need to express our speed in terms of something. 
# So we show the speed of the algorithm in terms of the input size. 
# That way, we can see how the speed reacts as the input size grows.

# Please look at big-O-complexity-chart.jpeg
# x axis: n represents the size of the data (number of elements)
# y axis: the number of operations
# So you're looking at how the number of operations changes, depending on the size of the data

# So big O notation for time complexity looks like:
# O(n)
# you just put a big O infront of the number of operations (n)
# Order of (n) would be linear time 
# The number of operations grows at the same rate as the input size
# (we will come back to this)

# Then you add alegbra to change the meaning
# O(n^2)
# Now the number of operations is growing at the rate of the square of the input size
# Oh no!

# Generally we don't care about speed when the input size is small. 
# The differences in speed are likely to be minimal when the input size is small.
# When the input size gets enormous, we can see the differences in efficiency between algorithms.

# Let's go through time complexity, from the fastest to the slowest!
