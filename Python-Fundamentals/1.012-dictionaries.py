# A dictionary is like a list, but instead of accessing values with an index, you access values with a "key."

myList = ["Jim", 32]
myDictionary = {"Name": "Jim", "Age":32}

print(myDictionary)

print(myList[1]) # 32
print(myDictionary["Age"]) # 32

print(len(myList)) # 2
print(len(myDictionary)) # 2

print(myDictionary.keys()) # dict_keys(['Name', 'Age'])

# You can check for a key with 'in':
print("Name" in myDictionary) # True



# A List is a collection which is ordered and changeable. Allows duplicate members.
# A Dictionary is a collection which is ordered and changeable. No duplicate members.

# (As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered)
# Good point - What python version for your test? Probably won't matter.

# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

myDictionary["Age"] = 33
print(myDictionary)

# A given key can appear in a dictionary only once. Duplicate keys are not allowed. 
# A dictionary maps each key to a corresponding value, so it doesn’t make sense to map a particular key more than once. 
# If you specify a key a second time during the initial creation of a dictionary, then the second occurrence will override the first.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# The values in dictionary items can be of any data type
# And almost any type of value can be used as a dictionary key in Python. 
# You can even use built-in objects like types and functions. 

def plusone(num):
  return num + 1

myDictionary = {
  "Name": "Jim", 
  "Age":32, 
  str(): "not sure why you'd do this", 
  plusone: "or this", 
  False: "or this..."
  }

print(myDictionary)

# However, a dictionary key must be of a type that is immutable. 
# For example, you can use an integer, float, string, or Boolean as a dictionary key. 
# However, neither a list nor another dictionary can serve as a dictionary key, because lists and dictionaries are mutable. 
# Values, on the other hand, can be any type and can be used more than once.

# Another way to construct a dictionary:

phonebook = {}  # creates an empty dictionary
phonebook["Abe"] = 4569874321
phonebook["Bill"] = 7659803241
phonebook["Barry"] = 6573214789

print(phonebook)
# {'Abe': 4569874321, 'Bill': 7659803241, 'Barry': 6573214789}

# Is just the same as:

phonebook = {
    "Abe": 4569874321,
    "Bill": 7659803241,
    "Barry": 6573214789
}

print(phonebook)
# {'Abe': 4569874321, 'Bill': 7659803241, 'Barry': 6573214789}

# Looping
# https://www.w3schools.com/python/python_dictionaries_loop.asp

# We can iterate over a dictionary as we iterated over a list
# The items() method will return each item in a dictionary, as tuples in a list.

for name, number in phonebook.items():
    print("Name: %s, Number: %s" % (name, number))

# Name: Abe, Number: 4569874321
# Name: Bill, Number: 7659803241
# Name: Barry, Number: 6573214789

# To remove a key-value pair from a dictionary, you need to use the del keyword or use the pop() method available on dictionary objects.
# The difference is pop() deletes the item from the dictionary and returns the value.
# When you use the del keyword, you've written a statement that doesn't evaluate to anything.

del phonebook["Abe"]

print(phonebook)  # {'Bill': 7659803241, 'Barry': 6573214789}

print(phonebook.pop("Bill"))  # 7659803241

print(phonebook)  # {'Barry': 6573214789}

print(len(phonebook))  # 1

# See Dictionary Methods here:
# https://www.w3schools.com/python/python_dictionaries_methods.asp


# ***************************************************************
# BONUS
# ***************************************************************

# https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.
# You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().

# Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in insertion order (if you want it sorted, just use sorted(d) instead).
# To check whether a single key is in the dictionary, use the in keyword.

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:


print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
# {'sape': 4139, 'guido': 4127, 'jack': 4098}

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:

print(dict(sape=4139, guido=4127, jack=4098))
# {'sape': 4139, 'guido': 4127, 'jack': 4098}


# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

dict_comprehension = {x: x**2 for x in (2, 4, 6)}

print(dict_comprehension)
# {2: 4, 4: 16, 6: 36}
