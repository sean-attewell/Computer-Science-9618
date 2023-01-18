# Lexical scope

# Lexical just means 'relating to the words or vocabulary of a language'
# The scope of a name binding (e.g. the name of a variable) is the part of a program where the name binding is valid
# that is, where the name can be used to refer to the entity. 
# The scope of a name binding is also known as the visibility of an entity
# Can you 'see' a binding depending on where you are?
# aka do you have access to it

# In other parts of the program, the same name may refer to a different entity, or to nothing at all.
# Scope helps prevent name collisions by allowing the same name to refer to different objects – as long as the names have separate scopes


# See python-scope.jpg
# The LEGB rule is a kind of name lookup procedure, which determines the order in which Python looks up names. 
# For example, if you reference a given name, then Python will look that name up sequentially in the local, enclosing, global, and built-in scope. 
# If the name exists, then you'll get the first occurrence of it.

# The widest scope of all is known as Built-in Scope
# All the special reserved keywords fall under this scope. 
# e.g. if, return, True, def... and so on
# Built in functions such as print() too
# We can call the keywords anywhere within our program without having to define them before use.

# Before actually executing the print() function, Python looks in the local, the enclosing, and the global scope first, 
# and if there is nothing named print, then Python finally looks into the built-in scope.


# This variable x is defined in the global scope
x = 5

# We can see it with the inbuilt function globals():
print(globals())

# NOTE: you will also see anything you have imported ready for use in the globals space

# You could define your own variable called print 
# And if you referenced it, Python would look at the global scope before the built-in scope


# Python doesn't have block scope 
# so anything declared in an if block has the same scope as anything declared outside the block
# It's all the global scope

a = 0
if True:
  print(a)   # 0
  a = 1
  print(a)   # 1
  
  b = 24

print(a)       # 1
print(b)       # 24 

# We can now find both a and b in the global scope!

# Whenever a variable is defined outside any function, 
# it becomes a global variable, and its scope is anywhere within the program.
# But unlike a normal block, a function also has it's own local scope!

# functions can see outside of themselves to the global scope:

def my_function():
  y = x + 2
  print(y)

my_function()
# 7

# if we assign a variable in a function, as we did with y
# the outer program can't access it
# If we tried to print y in the global space:
# print(y)
# NameError: name 'y' is not defined

# So functions can see outside of themselves
# but you can't see into functions
# Imagine they're surrounded by a one-way mirror

# But think of the one way mirror as having a return slot,
# Through which it can push out whatever the function returns
# So if we had returned y from my_function, 
# we could save it for use in a variable in the global scope

# The local variable can be accessed from a function within the function:

def myfunc():
  var_in_myfunc = 300

  def myinnerfunc():
    print(var_in_myfunc)
    var_in_myinnerfunc = "hiding in the inner function"

  myinnerfunc()

myfunc() 
# 300

# myinnerfunc() can see all the way out to the golbal scope to access x as well if you wanted to
# it makes sense that it can see out of it's own way mirror
# and then also through the one way mirror of the function that contains it 
# all the way to the global scope outside

# But the inner function ALSO has it's own local scope which the outer function cannot access!
# The outer function (myfunc in this case) can't see through the one way mirror surrounding the inner function
# So you could not access var_in_myinnerfunc from myfunc any more than you could access it from a global context

# Enclosing scope is a special scope that only exists for nested functions. 
# If the local scope is an inner or nested function, then the enclosing scope is the scope of the outer or enclosing function

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



