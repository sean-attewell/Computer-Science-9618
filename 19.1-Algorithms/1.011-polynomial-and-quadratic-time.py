# O(n^c) - Polynomial time complexity.	
# As the input size increases, the number of operations increases depending on the exponent

# Wait what are polynomials again? Quick math detour:

# A polynomial is a sum of a finite number of terms, where each term has a coefficient (any real number, positive or negative)
# multiplied by a variable, being raised to a non-negative integer power.
# 10x^7 + 15x^3 - 9x^2  + 9
# 10, 15, -9, and 9 are coefficients.
# 9 is a coefficient because the last term could be written as 9x^0

# If you have one term it's alled a monomial e.g. 10z^15, or pi.x^5
# Binomial has two terms e.g. 9a^2 -5
# etc.

# The degree of a given term of a polynomial is the power you're raising the term to
# e.g. 9a^2 -5 is a second degree term
# For a number on it's own like -5 you can either say the constant term, or the zero-degree term (since it can also be written as 5x^0)

# If someone asks for the degree of the entire polynomial, it is the degree of the term with the highest degree.
# e.g. 10x^7 + 15x^3 - 9x^2  + 9 the degree of the entire polynomial is 7th degree. It's a 7th degree polynomial.
# Standard form for polynomials is where you write the terms in degree order. Highest degree term followed by next highest degree term etc.

# Back to computer science:

# Polynomial time complexity O(n^c) is the general term
# But most frequently you will see the more specific form of polynomial time complexity of quadratic time O(n^2)
# which is a type of polynomial time complexity 

# Quadratic: involving the second and no higher power of an unknown quantity or variable.
# e.g. ax^2 + bx + c
# Quadratus is Latin for square.

# When do you see this?
# When you have nested loops within your algorithm
# Any time you see a loop within a loop, you should think of quadratic time complexity 
# O(n^2)
# ... Which isn't great as the input size grows, as you can see from the chart

data = [1,2,3,4,5]
for x in data:
    for y in data:
        print(x, y)

# The outer loop will run n times, and the inner loop will run n times for each iteration of the outer loop,
# which will give total n x n = n^2 prints.
# If the array has 5 items it will print 25 times (5^2)
# If the array has ten items, it will print 100 times (10^2).
# As you can see we doubled the input size from 5 to 10, 
# but the number of operations increased by a factor of 4


# Bubble sort is a great example of quadratic time complexity 
# as we see a loop within a loop

# With every new pass, the largest element in the list “bubbles up” toward its correct position.
# Bubble sort consists of making multiple passes through a list, comparing elements one by one, 
# and swapping adjacent items that are out of order.

# After i iterations the last i elements are the biggest, and ordered.

# In each iteration, sift through the unsorted section to find the maximum.

# unsorted  | biggest
# 3 1 5 4 2 | 6 7 8 9
# 1 3 4 2 | 5 6 7 8 9
# The 5 is bubbled out of the unsorted section

def bubble_sort(list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                swapped = True

# If any swap took place in a run through the array, then swapped will be set to true
# This causes the while loop to keep going, and it does another run through the array from the start
# If no swap occured the loop will terminate early because the list is already sorted

# Note that we are only looping until the penultimate item, as the final item has nothing to swap with to its right
# Also note the line which does the swapping saves us storing a third 'temp' variable


list_to_sort = [5, 3, 8, 6, 7, 2]

print(list_to_sort)
bubble_sort(list_to_sort)
print(list_to_sort)

# https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python
# Here is an optimised version, using two for loops:

def bubble_sort_optimised(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1): # Don't have an outer loop i to reference here if we used an outer while loop!
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array

# Unlike the earlier implementation of bubble sort, the inner loop reduces in size as it goes on
# Each step “bubbles” the largest element to the end of the array. 
# This means that each iteration takes fewer steps than the previous iteration 
# because a continuously larger portion of the array is already sorted.
# j initially goes from the first element in the list to the element immediately before the last. 
# During the second iteration, j runs until two items from the last, then three items from the last, and so on. 

# This implementation of bubble sort consists of two nested for loops in which the algorithm performs n - 1 comparisons, then n - 2 comparisons, and so on
# until the final comparison is done. 
# This comes at a total of (n - 1) + (n - 2) + (n - 3) + … + 2 + 1 = n(n-1)/2 comparisons, 
# which can also be written as ½n^2 - ½n.

# You learned earlier that Big O focuses on how the runtime grows in comparison to the size of the input. 
# That means that, in order to turn the above equation into the Big O complexity of the algorithm
# you need to remove the constants because they don’t change with the input size.
# Doing so simplifies the notation to n^2 - n. Since n^2 grows much faster than n, this last term can be dropped as well
# leaving bubble sort with an average- and worst-case complexity of O(n^2).


# Insertion sort! 
# Another quadratic time complexity sorting algorith specified in your syllabus
# I will try and stick closely to the implementation you provided

# https://realpython.com/sorting-algorithms-python/#the-insertion-sort-algorithm-in-python

# An excellent analogy to explain insertion sort is the way you would sort a deck of cards. 
# Imagine that you’re holding a group of cards in your hands, and you want to arrange them in order. 
# You’d start by comparing a single card step by step with the rest of the cards until you find its correct position. 
# At that point, you’d insert the card in the correct location 
# then start over with a new card, repeating until all the cards in your hand were sorted.

# After i iterations the first i elements are ordered.

# sorted  | unsorted
# 1 3 5 8 | 4 6 7 9 2
# 1 3 4 5 8 | 6 7 9 2

def insertionSort(array):
  for i in range(1, len(array)): 
    value = array[i]
    j = i - 1 

    while j >= 0 and array[j] > value:
      array[j + 1] = array[j]
      j = j - 1

    array[j + 1] = value

# Let us go through line by line:
# Define the function
# Loop through the array. We start the range at index 1, because index 0 has nothing to its left to swap with
# Grab the value which we are inserting
# Grab the index to its left
# While index to the left is bigger than or equal to zero (the start of the array)
# and the value to the left is bigger than the value we're sorting
# We move the value which was on the left over to the right by one to make space for the value we're inserting
# it doesn't matter that this overwrites the value we're sorting, because we've saved that in the variable 'value'
# But we don't insert it yet!
# we decrement the index j by one, as this is the next value to the left to check... 
# Having shifted all larger sorted elements to the right it's finally time to insert in the correct positioned
# When the value is in place, we go to the next item in the outer for loop

data = [9, 5, 1, 4, 3, 9, 7, 3, 45]
insertionSort(data)
print(data)


# Again it's a loop within a loop
# so you should immediately think of quadratic time O(n^2)

# Worst Case Complexity: O(n^2)
# Suppose an array is in descending order, In this case, worst case complexity occurs.
# Each element has to be compared with each of the other elements so, for every nth element, (n-1) number of comparisons are made.
# Thus, the total number of comparisons = n*(n-1) ~ n^2

# Although bubble sort and insertion sort have the same Big O runtime complexity, 
# in practice, insertion sort is considerably more efficient than bubble sort. 
# If you look at the implementation of both algorithms, then you can see how insertion sort has to make fewer comparisons to sort the list.
# Insertion Sort swaps the next avaiable value directly next to the sorted portion of the list
# stopping at the right place
# Bubble sort starts at the start of the list each time before bubbling the largest value up into the sorted portion
# Even we use the optimised bubble sort which stops making comparisons when it hits the sorted portion,
# it is still swapping through all remaining unsorted values each time


# https://www.interviewkickstart.com/learn/comparison-among-bubble-sort-selection-sort-and-insertion-sort

# Bubble sort can detect minor errors in a sorted dataset and sort an almost sorted dataset quickly.
# Insertion sort is used to sort online data — it can start the sorting process even if the complete data set isn’t available.

# Bubble sort makes many comparisons and swaps and thus is not efficient if swapping or comparison is a costly operation.
# Insertion sort makes a lot of swaps and thus becomes inefficient if swapping operations are costly.

