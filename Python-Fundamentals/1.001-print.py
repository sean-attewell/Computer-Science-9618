# console = physical terminal (text input/output environment)
# shell = command line interpreter (Tell your computer what to do without a graphical user interface!)

# Comments are ignored by python!

print("Hello World!") # You can comment after code too

# You can commentent out code so it doesn't run:
# print("this won't run.")

# It's common to use double quotes for strings so that you can include apostrophes without accidentally terminating the string.
my_string = "I don't have to worry about apostrophes with my double-quotes."

print(my_string)

# our first function - the print function
# This is an inbuilt function, not user defined
# Functions won't run unless you turn the key by putting brackets after them
# This is 'calling' the function
# Calling a function causes some other previously written code somwhere else to run
# () is called the call operator

print # this does nothing without the call operator. Press the button!

# Some functions, like the print function, take in data which we call arguments
# Any object passed as an argument into print will get converted into a string type before outputted to the screen.
# Multiple items can be separated by commas. print will use " " as the default separator value.

print("Multiple arguments", 2022, True, sep="!!!")
print("Multiple arguments", 2022, True, sep="")
print("Multiple arguments", 2022, True, sep="\t")  
print("Multiple arguments", 2022, True, sep="\n")

# In Python strings, the backslash "\" is a special character, also called the "escape" character. 
# It is used in representing certain whitespace characters: "\t" is a tab, "\n" is a newline

# You can store functions in a new variable
myVariable = print
myVariable('printing from a different variable name!')

# code is endless layers of abstraction
# things representing things representing things

