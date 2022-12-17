# Python's boolean values are written as True and False (make sure you capitalize the first character).

x = 10
print(x == 10)  # True
print(x == 5)  # False
print(x < 15)  # True
print(x > 15)  # False
print(x <= 10)  # True
print(x >= 10)  # True
print(x != 20)  # True

# The bool() function allows you to evaluate any value, and give you True or False in return,

hello = "Hello"
fifteen = 15

print(bool(hello)) # True
print(bool(fifteen)) # True

# Almost any value is evaluated to True if it has some sort of content.

# There are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. 
# And of course the value False evaluates to False

print(bool(False)) # False
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


# If we want to determine if two objects are actually the same instance in memory, we use the is operator instead of the value comparison operator ==.

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True because a and b have the same value
print(a is b)  # False because a and b reference two different list objects

x = [1, 2, 3]
y = x

print(x == y)  # True because x and y have the same value
print(x is y)  # True because x and y reference the same list object


# There is also the not operator, which inverts the boolean that follows it:

print(not False)    # True
print(not (1 == 1))  # False because 1 == 1 is True and then is inverted by not