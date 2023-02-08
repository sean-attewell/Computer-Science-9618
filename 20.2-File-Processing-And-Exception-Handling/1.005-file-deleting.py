# To delete a file, you must import the OS module
# and run its os.remove() function

# "Oh gosh, should I know what this module is? Why does this need a module?"
# The python docs say the os module is 'Miscellaneous operating system interfaces'.
# Nice.

import os
os.remove("killme.txt")

# No file object here to deal with like with file opening to reading and write
# We're getting rid of the file after all, so why would we have one?

# What if we try to run it again?
# FileNotFoundError: [WinError 2] The system cannot find the file specified: 'killme.txt'

# To avoid getting this error, you might want to check if the file exists before you try to delete it:

import os
if os.path.exists("killme.txt"):
  os.remove("killme.txt")
  print("💀 FILE DELETED 💀")
else:
  print("The file does not exist")

# Remember that the path is just the file name, as the file exists in the same folder.


# To delete an entire folder, use the os.rmdir() method:

# import os
# os.rmdir("myfolder")


# ***************************************************************
# BONUS
# ***************************************************************

# More on importing:

# You can just import the specific function you want to use, rather than the whole os module
# from os import remove
# Now you can call remove directly rather than having to type os.remove to access it
# remove("killme.txt")

# The 'as' keyword
# You can employ aliases to use a different name to that defined in the exporting module:
# from os import remove as r
# r("killme.txt")


from os import path as aliasforpath
from os import remove as kill

if aliasforpath.exists("killme.txt"):
  kill("killme.txt")
  print("💀 FILE DELETED 💀")
else:
  print("The file does not exist")


# likewise you can use an alias for the whole module

import os as aliasformodue

aliasformodue.remove("killme.txt")
