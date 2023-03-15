# Make a GroundVehicle class
# Provide a num_wheels attribute that can be specified at runtime
# Make num_wheels default to 4 if not specified when the object is constructed.
# add a method called drive() that returns "vroooom".


class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    def drive(self):
        return "vroooom"


# Subclass Motorcycle from GroundVehicle.

# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.

# Override the drive() method in Motorcycle so that it returns "BRRRRRR!!"

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels=2):
        super().__init__(num_wheels)

    def drive(self):
        return "BRRRRRR!!"


my_groundvehicle = GroundVehicle()
print(my_groundvehicle.num_wheels)

my_motorcycle = Motorcycle()
print(my_motorcycle.num_wheels)


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

for v in vehicles:
    print(v.drive())
