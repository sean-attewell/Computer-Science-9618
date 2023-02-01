# File Handling

# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# To open a file for reading it is enough to specify the name of the file:

f = open("demofile.txt")

# The code above is the same as:

f = open("demofile.txt", "rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.

# The open() function returns a file object, which has a read() method for reading the content of the file:

f = open("demofile.txt", "r")
print(f.read())

# The above works because demofile.txt is saved in the same folder
# And you are in that location in the terminal
# If the file was in a different location, you can specify the absolute or relative path:

f = open("D:\Computer-Science-9618\\20.2-File-Processing-And-Exception-Handling\demofile.txt", "r")
print(f.read())

# Be careful with \ as potentially signifying an escape character depending on what comes next.
# There is no harm in putting two blackslashes together just in case

# You can read .py files just the same! They are text after all.
# f = open("1.003-file-reading.py", "r")
# print(f.read())


# Return the 5 first characters of the file:

f = open("demofile.txt", "r")
print(f.read(5))

# Read two lines of the file:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())


# Loop through the file line by line:

f = open("demofile.txt", "r")
for x in f:
  print(x + "read one line")

# Close the file when you are finish with it:

f.close()

# what happens if we try print(f.read()) now?
# It won't work...

# Remeber we said that the 'finally:' clause in 'try' blocks are often used to make sure the file closes
# regardless of whether there is an exeption or not

