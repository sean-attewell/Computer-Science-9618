# This is mostly lifted from w3schools, with edits and additions
# https://www.w3schools.com/python/python_try_except.asp

# The try block lets you test a block of code for errors.

# The except block lets you handle the error - think of it as short for exception
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

#e.g.
# print(x)
# NameError: name 'x' is not defined

try:
  print(x)
except:
  print("An exception occurred")

# You can define as many exception blocks as you want
# e.g. if you want to execute a special block of code for a special kind of error:

try:
  print(3/0)
except NameError:
  print("Variable x is not defined!")
except ZeroDivisionError:
  print("The second operator in a division is zero!")
except:
  print("Something else went wrong")

# Check out python's built-in  execptions here:
# https://www.w3schools.com/python/python_ref_exceptions.asp

# You can use the else keyword to define a block of code to be executed if no errors were raised:

try:
  print("Try didn't raise an exception!")
except NameError:
  print("Variable x is not defined!")
except ZeroDivisionError:
  print("The second operator in a division is zero!")
except:
  print("Something else went wrong")
else:
  print("Since nothing went wrong, I'll do else as well!")


# Ulike else, The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# This is particularly useful for closing files when you're finished... which we will get to very shortly


# As a Python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword.
# You can define what kind of error to raise, and the text to print to the user.

y = -1

if y < 0:
  raise Exception("Sorry, no numbers below zero")

# Note that this stops the program, as there is no try/except block

# 'Exception' is the base class for all exceptions
# it can function as a generic exception to throw
# or you could specify one of the others that inherit from it:

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")