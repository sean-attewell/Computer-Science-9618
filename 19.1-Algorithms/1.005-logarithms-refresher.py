# Logarithm Fundamentals https://www.youtube.com/watch?v=cEvgcoyZvB4

# A lot of confusion comes from having 3 different notations to represent directly related ideas:

# With exponentials we represent them with the relative position of the number (e.g. 2^x), placing it in the upper right, in a smaller font
# When taking square roots or cube roots and so on, we introduce new notation with the radical symbol (√)
# And when dealing logarithms we insead use a word 'log', followed by an argument in brackets!!

# Why does it have to be this way???
# Accept it and move on.
# logarithm-notation.png shows clearly the relationship between logs and exponents

# 10^3 = 1000 --> What is 10 to the power of 3?
# I want the argument (answer)!

# 3√1000 = 10 --> What to the power of 3 is 1000?
# I want the base!

# log base10 (1000) = 3 --> 10 to the power of what is 1000?
# I want the exponent!

# think 'the log wants to find the exponent'
# "Base to the power of what is the argument?"
# “How many times do we multiply the base together to get the argument?"

# log base10 (1000) = 3 
# 10 to the power of what is 1000?
# 10 to the power of 3 is 1000
# What the log wants to be, is the exponent!

# In base 10, When you plug in powers of 10, logarithms are a zero counting function!
# log(0.1) = -1
# log(1) = 0
# log(10) = 1
# log(100) = 2
# log(1000) = 3
# ...
# log(1_000_000) = 6

# In each step as we multiply the input by 10, the output (the exponent we are looking for as the answer) only goes up in increments of 1. 
# ***There is very slow growth in output relative to the increase in input size***

# Think of how this is the opposite of base 10 exponentials:
# 10^0 = 1
# 10^1 = 10
# 10^2 = 100
# 10^3 = 1000
# ...
# 10^6 = 1_000_000

# In each step we are only increasing the input by 1, but the output increases by a factor of 10!
# ***There is very fast growth in output relative to the growth in input size***

# So far we have looked at examples in base 10, because they are intuitive
# But another source of confusion, is that the base is sometimes ASSUMED based on your field!!

# In maths generally a log without a specified the base will be log base e, also written as 'ln', the natural log.
# In engineering it's often assumed log base 10
# But in our wolrd of computer science, it usually means log base 2
# ...
# Good to know!

# log base2 (64) = 6
# to the power of what is 64?


# ***************************************************************
# BONUS
# ***************************************************************

# Here is a great video on this topic by 3Blue1Brown
# Awesome youtube channel at visualising math concepts
# It covers the 'alternate notation' idea 
# https://www.youtube.com/watch?v=cEvgcoyZvB4


# Think of a log price chart.
# Expontential growth is often plotted with a log scale.
# On a logarithmic scale, big growth is clearer to see
# Y axis goes up in where each step is multiplicitive (e.g. each step is 10x the previous level).
# The Y axis is now plotting not the total number of cases, but the logarithm of the total number of cases.

