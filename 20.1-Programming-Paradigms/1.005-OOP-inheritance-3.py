# A simple animal example for practise 
# Test yourself without looking to see which part of the structure of a class you might forget

class Animal:
    def __init__(self, name, breed, colour):
        self.name = name
        self.breed = breed
        self.colour = colour

    def __str__(self):
        return f"Name: {self.name} \ncolour: {self.colour} \nBreed: {self.breed} \n"


a = Animal("Groot", "Tree", "Brown")
print(a)

class Dog(Animal):
    def __init__(self, name, breed, colour, eyes, fluffy, good_boy=True):
        super().__init__(name, breed, colour)
        self.eyes = eyes
        self.fluffy = fluffy
        self.good_boy = good_boy

    def bark(self):
        print("Aggressive borking noises\n")

    def instructed_to_sit(self):
        if self.good_boy:
            print(f"the {self.breed} {self.name} sits patiently")
        else:
            self.bark()

barny = Dog("Barny", "Labrador", "Golden", "Has one eye", "Moderate fluff", True)

print(barny)
barny.bark()
barny.instructed_to_sit()
