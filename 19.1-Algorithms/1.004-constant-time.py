# Constant Time: O(1)
# No matter how large or small the input is (1,000,000 or 10 elements), the number of computations within the function is the same.
# The number of operations is unaffected by input size - it is constant!

my_list = ['thing 1', 'thing 2', 'thing 3', 'thing 4', 'thing 5']

def print_only_one_thing(list_of_things):
    print(list_of_things[0])

print_only_one_thing(my_list)  # thing 1

# Here the input list can get as big as you like
# But the number of operations will remain the same as we access the first item in the list only
# The number of operations is constant

# This is shown as a horizontal line on the graph... It doesn't grow as you increase the number of elements.