
# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

with open('demofile.txt', 'r') as f:
    read_data = f.read()
    print(read_data)

# Here is that 'as' keyword again!

# The above with statement will automatically close the file after the nested block of code. 
# The advantage of using a with statement is that it is guaranteed to close the file no matter how the nested block exits. 
# If an exception occurs before the end of the block, it will close the file before the exception is caught by an outer exception handler. 
# If the nested block were to contain a return statement, or a continue or break statement, 
# the with statement would automatically close the file in those cases, too.
# https://stackoverflow.com/questions/1369526/what-is-the-python-keyword-with-used-for

# If you’re not using the with keyword, then you should call f.close()
# to close the file and immediately free up any system resources used by it.