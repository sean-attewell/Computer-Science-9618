# https://www.programiz.com/python-programming/object-oriented-programming#:~:text=Python%20Encapsulation,helps%20to%20achieve%20data%20hiding.
# https://www.geeksforgeeks.org/encapsulation-in-python/
# https://www.tutorialsteacher.com/python/public-private-protected-modifiers

# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
# It describes the idea of wrapping data and the methods that work on that data within one unit. 
# This puts restrictions on accessing variables and methods directly, and can prevent the accidental modification of data. 

# Classical object-oriented languages, such as C++ and Java, control the access to class resources by public, private, and protected keywords
# All members in a Python class are public by default: Any member can be accessed from outside the class environment.
# When editing the adventure game we looked at for instance, you could use the classes freely, mutating their attributes at will.

# Protected:
# 'Protected' members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class 
# but can be accessed from within the class and its subclasses

# To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”.
# ... Except what are we really accomplishing?
# The protected variable can still be accessed outside of the class (as well as in the subclass) 
# But it is customary (convention not a rule) to not access the protected outside the class.
# So it's not really 'protected' other than by convention...
# You are relying on the user.

 
# Creating a base class
class Base:
    def __init__(self):
 
        # Protected member
        self._a = 2
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
 
        Base.__init__(self)
        print("Calling protected member of base class: ",
              self._a)
 
        # Modify the protected variable:
        self._a = 3
        print("Calling modified protected member outside class: ",
              self._a)
 
obj1 = Base()
obj2 = Derived()
 
# Accessing the protected variable outside
print("Accessing protected member of obj1: ", obj1._a) # 2

# Can be accessed but should not be done due to convention
print("Accessing protected member of obj2: ", obj2._a) # 3
 

# Private:
# The class members declared 'private' should neither be accessed outside the class nor by any subclass
# To prevent accidental change, an object’s variable can only be changed by an object’s method. 

# To define a private member in Python, prefix the member name with double underscore “__”.


class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# print(c.__maxprice)
# AttributeError: 'Computer' object has no attribute '__maxprice'

# But it can still be accessed through name mangling...
# instead of self.__var1, you have to write self._YourClassName__var1 
# print(c._Computer__maxprice)
# So, it can still be accessed from outside the class, but it has syntactical extra steps.

# change the price
c.__maxprice = 1000
c.sell()

# We have tried to modify the value of __maxprice outside of the class. 
# However, since __maxprice is a private variable, this modification is not seen on the output.

# using setter function
c.setMaxPrice(1000)
c.sell()

# To change the value, we have to use a setter function i.e setMaxPrice() which takes price as a parameter.

