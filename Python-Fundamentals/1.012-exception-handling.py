# Now we've covered a bunch of the basics, time for a fun little script!
# There are a few little things you might not have seen before
# but most important is the exception handling, which is a part of your syllabus 

# Let's see if we can hack together a little random number guessing game

# We'll need to generate a random number...
# so we import a module called 'random'
# Python has a built-in module that you can use to make random numbers. 
# the randrange()	method returns a random number between the given range
# Handy.

# We want the game to go on for as long as it takes for the player to win
# What kind of loop goes on indefinitely?

# A game should be interactive, so we want the user to be able to input data!
# The built-in input() function prompts the user for data that is converted to and returned as a string
# Python stops executing when it comes to the input() function, and continues when the user has given some input.

# Exception Handling
# When an error occurs (an exception as we call it), Python will normally stop and generate an error message.
# If however a 'try' block raises an error, the except block will be executed
# e.g. the try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")

# What if the player enters something that isn't a number?
# We don't want the game to crash!
# We want to give them another chance
# Remember how we end the current interation of a loop and _continue_ to the next one?
# We don't want to use the break keyword, that would end the loop completely!

# We can test to see the sort of error it gives, and specify that particular error.
# You can read more about exception handling here:
# https://www.w3schools.com/python/python_try_except.asp
# but we will come back to this when we get to file processing :)


import random

print("Welcome to ~*GUESS THE NUMBER!*~'")

secret_number = random.randrange(101)

while True:
  guess = input("Input your guess: ")
  
  try:
    guess = int(guess)
  except ValueError:
    print("Please enter an integer.")
    continue

  print(f"You guessed: {guess}")

  if guess == secret_number:
    print("You win!")
    break
  elif guess < secret_number:
    print("Too small!")
  else:
    print("Too big!")

