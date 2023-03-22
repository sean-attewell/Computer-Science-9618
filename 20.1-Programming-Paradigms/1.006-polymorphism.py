# https://stackoverflow.com/questions/1031273/what-is-polymorphism-what-is-it-for-and-how-is-it-used

# If you have been given a textbook definition of polymorphism for the A level I'd love to hear it
# "The provision of a single interface to entities of different types"

# But this stack overflow answer is my favourite explanation:

# Poly = many: polygon = many-sided, polystyrene = many styrenes (a), polyglot = many languages, and so on.
# Morph = change or form: morphology = study of biological form, Morpheus = the Greek god of dreams able to take any form.

# So polymorphism is the ability (in programming) to present the same interface for differing underlying forms (data types).

# For example, in many languages, integers and floats are implicitly polymorphic since you can add, subtract, multiply and so on, 
# irrespective of the fact that the types are different. They're rarely considered as objects in the usual term.
# But, in that same way, a class like BigDecimal or Rational or Imaginary can also provide those operations, 
# even though they operate on different data types.

# The classic example is the Shape class and all the classes that can inherit from it (square, circle, dodecahedron, irregular polygon, splat and so on).

# With polymorphism, each of these classes will have different underlying data. 
# A point shape needs only two co-ordinates (assuming it's in a two-dimensional space)
# A circle needs a center and radius. 
# A square or rectangle needs two co-ordinates for the top left and bottom right corners and (possibly) a rotation. 
# An irregular polygon needs a series of lines.

# By making the class responsible for its code as well as its data, you can achieve polymorphism. 

# In this example, every class would have its own Draw() function and the client code could simply do:
# shape.Draw()
# to get the correct behavior for any shape.

# This is in contrast to the old way of doing things in which the code was separate from the data
# and you would have had functions such as drawSquare() and drawCircle().

# Object orientation, polymorphism and inheritance are all closely-related concepts and they're vital to know. 


# https://www.programiz.com/python-programming/polymorphism

# **Operator polymorphism**

# We know that the + operator is used extensively in Python programs. But, it does not have a single usage:

num1 = 1
num2 = 2
print(num1+num2)

str1 = "Python"
str2 = "Programming"
print(str1+" "+str2)

# arithmetic addition or concatenation
# Here, we can see that a single operator + has been used to carry out different operations for distinct data types.


# **Function Polymorphism**

# There are some functions in Python which are compatible to run with multiple data types.
# One such function is the len() function:

print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))

# Here, we can see that many data types such as string, list, tuple, set, and dictionary can work with the len() function. 
# However, we can see that it returns specific information about specific data types.


# **Polymorphism in Class Methods**

# Python allows different classes to have methods with the same name:


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

# We can then later generalize calling these methods by disregarding the object we are working with:

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()


# Notice that we have not created a common superclass or linked the classes together in any way. 
# Even then, we can pack these two different objects into a tuple and iterate through it using a common animal variable. 
# It is possible due to polymorphism


# ***Polymorphism and Inheritance***

# Like in other programming languages, the child classes in Python also inherit methods and attributes from the parent class. 
# We can redefine certain methods and attributes specifically to fit the child class, which is known as Method Overriding.

# Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class.

from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())

# Here, we can see that the methods such as __str__(), which have not been overridden in the child classes, are used from the parent class.

# Due to polymorphism, the Python interpreter automatically recognizes that the fact() method for object a (Square class) is overridden. 
# So, it uses the one defined in the child class.

# On the other hand, since the fact() method for object b isn't overridden, it is used from the Parent Shape class.


# Remember... Polymorphism: 
# "The provision of a single interface to entities of different types"
