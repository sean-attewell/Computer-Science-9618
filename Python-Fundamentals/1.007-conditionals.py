# Now we have some of the basics down, lets put them to use in conditionals!
# if statements: "if this condition is true, then do this"
# Running the code is _conditional_ on something being true

# Python uses boolean values to evaluate conditions. 
# An expression in any Boolean context will evaluate to a Boolean value and then control your program's flow.


name = "Elon"
age = 51
if name == "Elon" and age == 51:
    print("You are a 51 year old person named Elon.")


# So in this case 'name == "Elon" and age == 51' is an expression
# being after the 'if' means it's in a boolean context
# python expects something to evaluate to true for false after the if
# "if X is true, then do this..."

if name == "Elon" or name == "Bill":
    print("Your name is either Elon or Bill.")


# Any time you have an iterable object (like a list), you can check if a specific item exists inside that iterable by using the in operator.

years = [2018, 2019, 2020, 2021]
year = 2020

if year in years:
    print(f"{year} is in the years collection")

# 2020 is in the years collection


# We can use the if, elif, and the else keywords to define a series of code blocks that will execute conditionally.

first_statement = False
second_statement = True

if first_statement:
    print("The first statement is true")
elif second_statement:
    print("The second statement is true")
else:
    print("Neither the first statement nor the second statement are true")
# At most, one of the code blocks specified will be executed.
# If an else clause isn’t included, and all the conditions are false, then none of the blocks will be executed

# You can string multiple elif clauses together in a row if you like

if 'a' in 'bar':
    print('foo')
elif 1/0:
    print("This won't happen")
# elif var:
#     print("This won't either")

# prints foo
# The second expression contains a division by zero, and the third references an undefined variable var.
# Either would raise an error, but neither is evaluated because the first condition specified is true.


# ***************************************************************
# BONUS
# ***************************************************************

# Python’s Ternary Operator
# Goood for performing a simple if statement on a single line

# <expr1> if <conditional_expr> else <expr2>

# <conditional_expr> is evaluated first. If it is true, the expression evaluates to <expr1>. 
# If it is false, the expression evaluates to <expr2>.
# Notice the non-obvious order: the middle expression is evaluated first, and based on that result, one of the expressions on the ends is returned

raining = True
whereAreWeGoing = 'library' if raining else 'beach'
print(f"Let's go to the {whereAreWeGoing}")
# Let's go to the library

raining = False
print("Let's go to the", 'beach' if not raining else 'library')
# Let's go to the beach
# Here the ternary is evaluated into a single argument for the print statement (the second argument)

# Conditional expressions also use short-circuit evaluation like compound logical expressions. 
# Portions of a conditional expression are not evaluated if they don’t need to be.

# In the expression <expr1> if <conditional_expr> else <expr2>:

# If <conditional_expr> is true, <expr1> is returned and <expr2> is not evaluated.
# If <conditional_expr> is false, <expr2> is returned and <expr1> is not evaluated.


# Conditional expressions can also be chained together, as a sort of alternative if/elif/else structure, as shown here:
x = 4
s = ('foo' if (x == 1) else
     'bar' if (x == 2) else
     'baz' if (x == 3) else
     'qux' if (x == 4) else
     'quux'
     )

print(s) # qux

