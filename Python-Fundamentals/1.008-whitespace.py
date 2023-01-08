# http://www.ibiblio.org/g2swap/byteofpython/read/logical-and-physical-lines.html

# A physical line is what you see when you write the program. 
# A logical line is what Python sees as a single statement. 
# Python implicitly assumes that each physical line corresponds to a logical line.

#  you want to specify more than one logical line on a single physical line, then you have to explicitly specify this using a semicolon (;) 
#  which indicates the end of a logical line/statement.

i = 5
print(i)

# can also be written on one line as:

i = 5; print(i)

# ...But the idea is to avoid the semicolon as far as possible since it leads to more readable code
# This makes python look nice and clean

# You can also do the opposite, and split one logical line over multiple physical lines:
print \
(i)

# But please try not to.
# It might however be helpful when dealing with very long strings:

s = 'Pretend this is a really long string. \
This continues the string.'
print(s)

# but don't get \ confused with \n ... :)

print('This is written \
over 2 physical lines, but printed on one line')
print('this is written on one pysical line but\nprinted over 2 lines')


# In python, Whitespace (indentation) can denote code blocks.
# Python gives meaning to the amount of whitespace (indentation level) that comes before a logical line of code.


if True:
    print('This is 4 spaces')
    print('So this must also be 4 spaces')

# The mismatch of tab usage and spaces raises an error when Python tries to interpret the code.


# Javascript for example, looks like this:

"""
let hour = 12

if (hour < 18) {
  console.log("Good day");
} else {
  console.log("Good evening");
}
"""

# You need the curly braces to make the code run, because the language is not whitespace sensitive
# But you're still having to indent to make it human readable
 
# You could write the same javascript like this all on one line and it would still run:
# if (hour < 18) {console.log("Good day")} else {console.log("Good evening")};
# or even this runs fine:
# if(hour < 18){console.log("Good day")}else{console.log("Good evening")};

# You will also notice the end of a statement having a semi colon in Javascript
# As we've seen, Python doesn't need this unless you want multiple logical lines on one physical line. 
# Whitespace is instead used to denote the end of a logical line of code. 
# A logical line of code's end is marked by a '\n' (newline).


# The Python pass Statement

# Occasionally, you may find that you want to write what is called a code stub: 
# a placeholder for where you will eventually put a block of code that you haven’t implemented yet.

# In languages where token delimiters are used to define blocks, like the curly braces in Javascript, Perl and C, 
# empty delimiters can be used to define a code stub. For example, the following is legitimate Javascript code:

"""
let hour = 12

if (hour < 18) {} 
else {
  console.log("Good evening")
}
"""
# Here, the empty curly braces define an empty block.
# if hour < 18 is true, it will quietly do nothing.

# Because Python uses indentation instead of curly braces, it is not possible to specify an empty block.
# If you introduce an if statement with if <expr>:, something has to come after it, either on the same line or indented on the following line.
# Otherwise you get "IndentationError: expected an indented block"

# The Python pass statement solves this problem. It doesn’t change program behavior at all.
# It is used as a placeholder to keep the interpreter happy in any situation where a statement is syntactically required, but you don’t really want to do anything:

number = 0

if number > 0:
    print("Positive number")
elif number == 0: 
    pass 
else:
    print('Negative number')

# The elif path will quietly do nothing


# There is not a single situation in any country, in any programming language, or at any skill level, 
# in which is it acceptable to not indent your code the way Python requires it. 
# Therefore, it is technically redundant to have a language that is not whitespace-sensitive. 
# Any language that is not whitespace-sensitive requires (by universal convention) that programmers 
# communicate the scoping of the code in two distinct manners for every single line of code: braces (or begin/end) and indentation. 
# You are required to make sure that these two things match up, 
# and if you don’t, then you have a program that doesn’t work the way it looks like it works, and the compiler isn’t going to tell you.

# When you really analyse it, Python’s whitespace sensitivity is actually the only logical choice for a programming language, 
# because you only communicate your intent one way, and that intent is read the same way by humans and computers. 
# The only reason to use a whitespace-insensitive language is that that’s the way we’ve always done things, and that’s never a good reason.



# ***************************************************************
# BONUS
# ***************************************************************

# You may need to use it in an interactive session

# A widely used way to run Python code is through an interactive session. 
# To start a Python interactive session, just open a command-line or terminal and then type in python, or python3 depending on your Python installation, and then hit Enter.

# The standard prompt for the interactive mode is >>>, so as soon as you see these characters, you’ll know you are in.
# Now, you can write and run Python code as you wish, with the only drawback being that when you close the session, your code will be gone.


# >>> import string
# >>> string.whitespace
# ' \t\n\r\x0b\x0c'
# >>>

# Notice the characters are " " (space), \t (tab), \n (newline), \r (return), \x0b (unicode line tabulation), and \x0c (unicode form feed).
# You've seen the different types of whitespace characters that can appear, but you mainly need to concern yourself with " ", \t, and \n.


# Whitespace is used to denote the end of a logical line of code. 
# In Python, a logical line of code's end (a statement or a definition) is marked by a \n.

# In an interactive session you can write one line over mutliple lines using '\' as below
# >>> first = "Night"
# >>> second = "School"
# >>> first + second
# 'NightSchool'
# >>> first \
# ... + \
# ... second
# 'NightSchool'
# >>>
