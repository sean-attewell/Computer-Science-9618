# Most significant term

def do_different_things_in_the_same_function(list_of_things):  # O(n + n^2)
    # print all each item in the list
    for thing in list_of_things:  # O(n)
        print(thing)

    # print every possible pair of things in the list
    for thing_one in list_of_things:  # O(n * n) = O(n^2)
        for thing_two in list_of_things:
            print(thing_one, thing_two)

list_of_things = ['thing 1', 'thing 2', 'thing 3', 'thing 4', 'thing 5']

do_different_things_in_the_same_function(list_of_things)

# We could describe this function as O(n + n^2); 
# however, we only need to keep the most significant term, n^2
# So we would simply describe the big O time complexity as O(n^2)
# Why do we do this? 
# Because as the input size (n) gets larger and larger, the less significant terms have less effect, and only the most significant term is important.

# Again, this doesn't mean that it won't make a meaningful difference to the real runtime at smaller input sizes.
# But for the sake of big O, we only care about what makes the real difference as the input size grows very large