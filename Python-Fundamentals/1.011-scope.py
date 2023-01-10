# This variable x is defined in the global scope

x = 5

# functions can see outside of themselves to the global scope:

def my_function():
  y = x + 2
  print(y)

my_function()
# 7

# The function also has it's own local scope
# if we make a variable in a function, as we did with y
# the outer program can't access it
# If we tried to print y in the global space:
# print(y)
# NameError: name 'y' is not defined

# So functions can see outside of themselves
# but you can't see into functions
# Imagine they're surrounded by a one-way mirror
# You can only see what they push out through the return slot!

# The local variable can be accessed from a function within the function:

def myfunc():
  var_in_myfunc = 300

  def myinnerfunc():
    print(var_in_myfunc)

  myinnerfunc()

myfunc() 
# 300

# myinnerfunc() can see all the way out to the golbal scope to access x as well if you wanted to
# it makes sense that it can see out of it's own way mirror
# and then also through the one way mirror of the function that contains it 
# all the way to the global scope outside

# But what if the same variable name exists inside the function locally, and also globally?

z = "bar"

def test():
  z = "foo"
  print("z from inside the function:", z)

test()
# z from inside the function: foo

print("z from outside the function:", z)
# z from outside the function: bar

# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, 
# one available in the global scope (outside the function) and one available in the local scope (inside the function)
# Python checks the local scope for a variable called z FIRST, and if it's there, that's what it uses.

# Analogy: knowing two people both named Andrew. They have the same first name, but different last names.
# In the code above, the last name of the function x would be test, 
# while the last name of the top-level x would be global.
# In general, it's best to keep the names different anyway, to avoid confusion.






# ***************************************************************
# BONUS
# ***************************************************************

# There is an inbuilt function 'locals()' which will show you what variables are local to the context it is called

a_global_variable = 5

def my_function2():
  a_local_variable = a_global_variable + 2
  print(locals())

my_function2()
# {'a_local_variable': 7}