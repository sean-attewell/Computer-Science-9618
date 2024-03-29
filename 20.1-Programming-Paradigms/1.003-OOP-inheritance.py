# A class can inherit attributes and behaviour methods from another class, called the superclass.
# Also called the parent class or base class 
# A class which inherits from a superclass is called a child class, subclass or derived class

# https://www.w3schools.com/python/python_inheritance.asp

# Any class can be a parent class

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


# Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

# Inheritance models what is called an 'is a' relationship. 
# A student is a person
# This means that when you have a Derived class that inherits from a Base class, 
# you created a relationship where Derived is a specialized version of Base.


# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# The child's __init__() function overrides the inheritance of the parent's __init__() function.

class Student(Person):
  def __init__(self, studentID):
    self.studentID = studentID


y = Student(123)
print(y.studentID) # 123
# print(y.firstname) # AttributeError: 'Student' object has no attribute 'firstname'


# Python also has a super() function 
# The super() function returns an object that represents the parent class.


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

z = Student("Mike", "Olsen", 2019)
z.printname()
print(z.graduationyear)

# Q: Why does the __init__ on line 49 not need self?
# A: Because it is being called, not defined!

# The student __init__ method is called automatically when we instantiate the class
# and it's the student __init__ method that calls the parent __init__ method 
# So there is a chain reaction!

 
# Let's add some methods to the child class...

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

  def printname(self):
    print(self.firstname, self.lastname, "is a student")

a = Student("Joe", "Bloggs", 2023)
a.welcome()

# If you add a method in the child class with the same name as a function in the parent class, 
# the inheritance of the parent method will be overridden!

a.printname()

# The new printname() runs instead of the parent printname()
# This is just the same as the child __init__ running instead of the parent __init__
# And in just the same way, if we need to access the superclass method from the subclass, we use the super() method again.

class Animal:
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):
    
    # override eat() method
    def eat(self):
        
        # call the eat() method of the superclass using super()
        super().eat()
        
        print("I like to eat bones")

# create an object of the subclass
labrador = Dog()

labrador.eat()

# You could just call Animal().eat() instead of super().eat()...
# But since we do not need to specify the name of the base class when we call super()
# we can easily change the base class name (if we need to)

# Method Resolution Order (MRO) is the order in which methods should be inherited in the presence of multiple inheritance. 
# You can view the MRO by using the __mro__ attribute.

print(Dog.__mro__)
# (<class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>)

# ***************************************************************
# BONUS
# ***************************************************************

# Multiple inheritance 

class A:        # define your class A
  pass
class B:         # define your class B
  pass
class C(A, B):
  pass   # subclass of A and B

# Let me know if you need to cover this and we can go into a proper example!