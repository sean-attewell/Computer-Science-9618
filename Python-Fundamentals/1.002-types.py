# Python is a dynamically typed language, not a statically typed language
# You don't have to declare a variable's type
# In the C language for example, you'd have to specify that something is an integer: "int myNum = 15;"

# Type casting is a method used for changing the variables / values declared in a certain data type into a different data type 
# in order to match for the operation required to be performed by the code snippet. 
# In python, this feature can be accomplished by using the constructor functions like int(), string(), float(), etc. 
# Think of casting a spell on something to change it into what you need
# The execution of the type casting process can be performed by using two different types of type casting:
# implicit type casting and explicit type casting.

# implicit type Casting
 
# Python automatically converts
# a to int
a = 7
print(type(a))

# NOTE: We have just called a function inside of a function!
 
# Python automatically converts
# b to float
b = 3.0
print(type(b))
 
# Python automatically converts
# c to float as it is a float addition
c = a + b
print(c)
print(type(c))


# Explicit type casting:

my_int = 3
my_int2 = int(3.0)
print(my_int, my_int2)

my_float = 3.0
my_float2 = float(3)
print(my_float, my_float2)

my_string = str(89.33)

# print(my_string + 55) TypeError: can only concatenate str (not "int") to str
print(my_string + "concatenate another string") # this works!