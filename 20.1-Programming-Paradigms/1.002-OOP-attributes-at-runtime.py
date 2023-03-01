# https://www.hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-i/tutorial/

# You can also provide the values for the attributes at runtime 
# This is done by defining the attributes inside the init method
# (don't panic we will explain more after seeing it in action)

class Snake:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This is an instance of the Snake class called {self.name}"

    def change_name(self, new_name):
        self.name = new_name

# Now you can directly define separate attribute values for separate objects. For example:

# two variables are instantiated
python = Snake("python")
anaconda = Snake("anaconda")

# print the names of the two variables
print(python.name)  # python
print(anaconda.name)  # anaconda

anaconda.change_name("Adder")
print(anaconda.name)  # Adder

print(anaconda)  # This is an instance of the Snake class called Adder


# But what's all this funny looking double underscore stuff then?

# We've got two methods defined in our class with names that look like: __foo__ 
# They have double leading and trailing underscores
# doube underscores are called "dunders"
# You may hear these methods referred to as 'magic methods'
# It's just a way for Python to use names that won't conflict with user generated names you might make.
# They're reserved for special use in the language, like __init__
# It's just a convention and doesn't mean anything to the Python interpreter
# So avoid naming your own methods with dunders to avoid collisions!


# What's this __init__ thing then?

# class instantiation automatically invokes the __init__() method 
# it runs right after the object is created
# Think 'initialise'
# To instantiate a class, we simply call the class as if it were a function, passing the arguments that the __init__ method defines.
# This way we are able to provide a different name to each object we created in our example
# __init__ basically contains assignment statements


# What's this 'self' thing then?

# The self parameter is a reference to the current instance of the class
# Whatever the current object being instantiated or used is, that's what it points to.

# In the above example the python and anaconda objects have different names
# Even though the class they are made from has only one __init__ function
# self.name refers to that particular instance as self when set
# If there was no self argument, the same class couldn't hold the information for both these objects

# Likewise both python and anoconda instances have the exact same change_name function
# but self.name = new_name only sets it for the specific instance calling it

# If you don’t provide self, it will cause an error.
# It is only self by convention, you can call it whatever you like in theory
# but it has to be the first parameter of any function in the class
# for the love of god call it self though


# What's this __str__ thing then?

# This method is supposed to return a human-readable format which is used to display some information about the object
# The python __str__ method returns the string representation of the object. 
# The same method is also called when the str() or print() function is invoked on an object

print(python.__str__()) # This is an instance of the Snake class called python
print(str(python))      # This is an instance of the Snake class called python
print(python)           # This is an instance of the Snake class called python

# If we hadn't defined a __str__ method, calling the __str__ method would call the default __repr__ method... 


# What's this __repr__ thing then?

# repr is abbreviation of representation 
# The Python __str__ method returns the user readable string form of an object that can be understood by the end users. 
# However, the __repr__ method in python also returns a string representation of an object 
# which can be used for debugging purposes and development and it must be unambiguous.

# You can see the __str__ as a method for end users and __repr__ as a method for developers

print(python.__repr__()) # <__main__.Snake object at 0x0000025564D82FD0>
print(repr(python))      # <__main__.Snake object at 0x0000025564D82FD0>


# ***************************************************************
# BONUS
# ***************************************************************

# You can also change object attributes more directly like so:

# python.name = "Rattlesnake"
# print(python)

# del python.name
# print(python)
