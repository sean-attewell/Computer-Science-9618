# A function is a block of related statements, which together does some specific task. 

# If you keep writing the same sequence of operations over and over...
# You can put them into one handy function!
# You can then call it any time to perform all the operations at once for you

# Think of a function as a mini script to call
# It helps us avoid repetition, and organises code into manageable chunks
# If you ever find repetition when you're coding, this is a red flag!

# I think i've come up with a better analogy for calling a function...
# Calling a function with open and close brackets
# looks like putting your hands up around your mouth to CALL out to the code written elsewhere
# You can call out any arguments out to it - you shout these into the brackets (between your hands)
# ...
# Am I talking nonsense or is that quite good?

# So you want to build your own function...
# Define it with def!

def function_name(parameter_1):
  print(f"I have run the function_name function, with argument '{parameter_1}'")

function_name("my_argument_passed_to_the_function_parameter_1")

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.


def greet(name, greeting):
    print(f"Hello {name}, {greeting}")

greet("Ana", "I hope you are having an excellent day!")

# so what is the function name here? 
# What are the parameters?
# What are the arguments?

# Keyword Arguments (kwargs)
# You can also send arguments with the key = value syntax.
# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
# This way the order of the arguments does not matter.

def my_function(child1, child2, child3):
    print("The youngest child is " + child3)

my_function(child2="Tobias", child3="Linus", child1="Emil")


# You can send any data types of argument to a function (string, number, list, dictionary etc.) 
# and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def food_printer(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

food_printer(fruits)


# Note that the prior examples have just printed to the console
# This is an example of what would be called a 'side effect' of running a function
# This is not the same as the function returning a value

# Sometimes a function has an observable effect in some way
# it might display values in the console, modify a mutable (changable) data structure like a list, modify a file, or produce graphics. 
# This is called a side effect.
# Side effects are different from returned values because they are not the output.
# Many side effects can occur in one function. 
# A function, however, can return only one value.
# Importantly, returned values can be used in future computations. Side effects cannot.

# So arguments are the input to a function, but 
# If we want to define a function that returns a value to the caller, we use the return keyword.

def double(x):
    return x * 2

# you can assign what a function returns to a variable to play around with

returned_by_function = double(4)
print(returned_by_function)

# if a function doesn't return anything (only has side effects), it will retun None

variable = print("A thing to print")
print(variable)

# None is a special constant in Python that represents the absence of a value 
# It is an object of its own datatype


# Functions have to be defined before they are called...
# That probably sounds obvious
# But in other languages such as JavaScript for example, that's not the case!


# ***************************************************************
# BONUS
# ***************************************************************

# In Python, the number of arguments passed to the function call has to match the number of parameters defined in the function definition 

# def greet(name, greeting):
#     print(f"Hello {name}, {greeting}")

# greet("Anna") 
# This throws an error:
# TypeError: greet() missing 1 required positional argument: 'greeting'

# Do you know a way around this?
# Hint: there are 3!

# You could assign default values to the parameters in the function definition:

def greet2(name, greeting="u ok hun?"):
    print(f"Hello {name}, {greeting}")

greet2("Sean", "I hope you are having an excellent day!")
greet2("Sean")


# Alternatively, if the number of arguments is unknown, add a * before the parameter name
# This is known as 'Arbitrary Arguments' (*args)

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")  # linus

# You access the arguments the same way we've seen you access a list 
# (though it's actually a tuple, which we've not covered yet)


# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

def my_function3(**kid):
    print("His last name is " + kid["lname"])


my_function3(fname="Tobias", lname="Refsnes")