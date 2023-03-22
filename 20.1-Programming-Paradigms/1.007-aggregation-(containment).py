# https://isaaccomputerscience.org/concepts/prog_oop_aggregation_composition?examBoard=all&stage=all

# Aggregation (containment) and composition

# Within an OOP system, most classes will be associated in some way. 
# Association defines a relationship between two entirely separate classes.

# Aggregation (also known as containment) is a specialised form of association. 
# It defines a one-way relationship that specifies a 'has-a' relationship between two classes. 
# For example, you can say that a wallet has money. However, the money does not need a wallet in order to exist, so the relationship is one-way. 

# In a financial management game, if you deleted the wallet, the money would continue to exist.
# In the example of the card game, the relationship between a hand and a card is one of aggregation. 
# A hand has a card (in fact, it usually has more than one).

# Note how this differs from the inheritance relationship we looked at before
# A dog class may be the child class of an animal superclass
# this is because a dog *IS* an animal
# An animal does not *HAVE* a dog

# Aggregation acknowledges that the two classes have their own life cycle (i.e. can exist without each other). 
# Each object is instantiated separately. 
# In the example of a hand of cards, the cards will already exist before they are added to a Hand class. 

# game_deck = Deck()
# player_hand = Hand()
# …
# …
# dealt_card = game_deck.deal()
# player_hand.receive(dealt_card)

# Adding a card (to a Hand) will involve sending a message to the Deck to deal a card 
# and then using the Hand's receive method  to add it to the collection of cards that make up the Hand. 


# Where is my real code example??
# Check the adventure game folder!

# Here is another great example:
# https://www.geeksforgeeks.org/python-oops-aggregation-and-composition/

# "we are not creating an object of the Salary class inside the EmployeeOne class, 
# rather than that we are creating an object of the Salary class outside and passing it as a parameter of EmployeeOne class"



# ***************************************************************
# BONUS
# ***************************************************************

# Composition doesn't appear on your syllabus 

# Composition is a stricter form of association. 
# It defines a one-way relationship that specifies an 'is-part-of' relationship between two classes.
# For example, you can say that a room is part of a house. The rooms cannot exist outside of the house. 
# In a town planning simulation, if you deleted a house object, the rooms would also be deleted.

