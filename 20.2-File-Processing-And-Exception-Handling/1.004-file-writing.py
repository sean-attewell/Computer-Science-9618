# To write to an existing file, you must add an argument to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# remember that both create the file if it does not exist

f = open("demofile2.txt", "a") 
f.write("...Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

# What happens if we keep running the above?


# write will overwrite the original content of the existing file

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the original content!")
f.close()

# open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())