# https://realpython.com/python-getter-setter/

# Getter: A method that allows you to access an attribute in a given class
# Setter: A method that allows you to set or mutate the value of an attribute in a class

# In OOP, the getter and setter pattern suggests that public attributes should be used only 
# when you’re sure that no one will ever need to attach behavior to them. 
# If an attribute is likely to change its internal implementation, then you should use getter and setter methods.

# Implementing the getter and setter pattern requires:

# Making your attributes non-public
# Writing getter and setter methods for each attribute
# e.g.

class Label:
    def __init__(self, text, font):
        self._text = text
        self._font = font

    def get_text(self):
        return self._text

    def set_text(self, value):
        self._text = value

    def get_font(self):
        return self._font

    def set_font(self, value):
        self._font = value


# Typically, getter methods return the target attribute’s value, 
# while setter methods take a new value and assign it to the underlying attribute.

# To understand where getter and setter methods come from, get back to the Label example 
# and say that you want to automatically store the label’s text in uppercase letters.
# Unfortunately, you can’t simply add this behavior to a regular attribute like .text. You can only add behavior through methods, 
# but converting a public attribute into a method will introduce a breaking change in your API.


class Label:
    def __init__(self, text, font):
        self.set_text(text)
        self.font = font

    def get_text(self):
        return self._text

    def set_text(self, value):
        self._text = value.upper()  # Attached behavior

label = Label("Fruits", "JetBrains Mono NL")
print(label.get_text())
# 'FRUITS'

label.set_text("Vegetables")
print(label.get_text())
# 'VEGETABLES'

# Adding getter and setter methods to your classes can considerably increase the number of lines in your code. 
# Getters and setters also follow a repetitive and boring pattern that’ll require extra time to complete. 
# This pattern can be error-prone and tedious. 
# You’ll also find that the immediate functionality gained from all this additional code is often zero.


# The Pythonic way to attach behavior to an attribute is to turn the attribute itself into a property. 
# Properties pack together methods for getting, setting, deleting, and documenting the underlying data. 
# Therefore, properties are special attributes with additional behavior.

# You can use properties in the same way that you use regular attributes. 
# When you access a property, its attached getter method is automatically called. 
# Likewise, when you mutate the property, its setter method gets called. 
# This behavior provides the means to attach functionality to your attributes without introducing breaking changes in your code’s API.

# As an example of how properties can help you attach behavior to attributes, 
# say that you need an Employee class as part of an employee management system. 
# You start with the following bare-bones implementation:


class Employee:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

# Employee allows you to create instances that give you direct access to the associated name and birth date. 
# Note that you can also mutate the attributes by using direct assignments.

# As your project evolves, you have new requirements. 
# You need to store the employee’s name in uppercase letters and turn the birth date into a date object. 
# To meet these requirements without breaking your API with getter and setter methods for .name and .birth_date, you can use properties:

from datetime import date

class Employee:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = date.fromisoformat(value)


# In this enhanced version of Employee, you turn .name and .birth_date into properties using the @property decorator. 
# Now each attribute has a getter and a setter method named after the attribute itself. 
# A neat feature of properties is that you can use them as regular attributes:

john = Employee("John", "2001-02-07")

print(john.name)
# 'JOHN'

print(john.birth_date)
# 2001-02-07

john.name = "John Doe"
print(john.name)
# 'JOHN DOE'

# Cool! You’ve added behavior to the .name and .birth_date attributes without affecting your class’s API. 
# With properties, you’ve gained the ability to refer to these attributes as you would to regular attributes. 
# Behind the scenes, Python takes care of running the appropriate methods for you.

# You must avoid breaking your user’s code by introducing changes in your APIs. 
# Python’s @property decorator is the Pythonic way to do that

# Python developers tend to design their classes’ APIs using a few guidelines:

# Use public attributes whenever appropriate, even if you expect the attribute to require functional behavior in the future.
# Avoid defining setter and getter methods for your attributes. You can always turn them into properties if needed.
# Use properties when you need to attach behavior to attributes and keep using them as regular attributes in your code.
# Avoid side effects in properties because no one would expect operations like assignments to cause any side effects