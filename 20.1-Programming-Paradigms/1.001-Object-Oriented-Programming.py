# In object-oriented programming (OOP), an object is essentially an instance of a class
# Think of a class as a blueprint or template that you can use to create objects.

# A Python object encapsulates variables (data) and functions (behavior) into a single entity.
# An object instance gets its variables and functions from the class that was used to 'instantiate' it.


class MyFirstClass:
  """A simple example class"""

  variable = "data"

  def method(self):
    return "Printing from a MyFirstClass object."

# First in triple quotes we can see a docstring belonging to the class
# A Python docstring is a string used to document a Python module, class, function or method, 
# so programmers can understand what it does without having to read the details of the implementation
# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module
# they are associated with the object as their __doc__ attribute
# We can later use this attribute to retrieve the docstring.

# https://www.programiz.com/python-programming/docstrings
# If we don't assign strings to a variable, they can act as comments
# but unlike actual comments (like the one you're reading now), they are not ignored by the Python interpreter
# If it was ignored it couldn't be used as an attribute

# We can also use triple quotation marks for multi-line strings.
'''
I am a
multi-line comment!
'''
# Even though our example above is single-lined, we still use the triple quotes 
# around the docstring by convention, as they can be expanded easily later

# Next we assigned a variable in the normal manner
# variable = "data"

# Finally we defined a function
# You will hear functions that are defined within classes referred to as 'methods'
# A method is a function that “belongs to” an object.

# As you can see above, the way we defined the function within the class was no different to normal...
# Other than that mysterious parameter 'self'... which we will come back to.


# Instantiating a class in Python is simple. 
# To instantiate a class, we simply call the class as if it were a function:
 
a_class_object = MyFirstClass()

# The return value will be the newly created object.
# As you can see we assigned this newly created object to the variable name 'a_class_object'.

print(a_class_object.variable)  # data
print(a_class_object.method())  # Printing from a MyFirstClass object.

# In general, a dot expression is written as <expression>.<name>. 
# The <expression> must evaluate to an object, and the name must be an attribute on that object.

# But there is one more valid attribute we forgot!

print(a_class_object.__doc__) # A simple example class

# See how the inbuilt print function has it's own docstring too!
# print(print.__doc__)


# So hopefully you can see how broadly speaking:
# "instantiation is the creation of a real instance or particular realisation of an abstraction or template, such as a class"


# But the whole point of defining a class is so that you can use the same template to create multiple objects.
# All of the objects you make by instantiating the class will have the attributes that were a part of the class definition.

another_class_object = MyFirstClass()

print(another_class_object.variable)  # data
print(another_class_object.method())  # Printing from a MyFirstClass object.
print(another_class_object.__doc__) # A simple example class

# But why have two identical objects with the exact same data and behaviour?...
# Even identical twins have different names
# Two identical cars have different vehicle registrations


# ***************************************************************
# BONUS
# ***************************************************************

# You can access attributes directly from the class in the same way 
# as we have been from the object the class instantiates

# print(MyFirstClass.variable)
# print(MyFirstClass.__doc__)
# print(MyFirstClass.method.__doc__)