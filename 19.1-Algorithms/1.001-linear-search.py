# What is an algorithm?
# An algorithm is a set of instructions for accomplishing a task. 
# Within this broad definition, we could call every piece of code an algorithm.

# We will be looking at algorithms for searching, sorting, inserting and deleting.

# The simplest searching algorithm is linear search.
# Linear search is a sequential searching algorithm where we start from one end and check every element of the list until the desired element is found.

# Start from the leftmost element of and one by one compare x with each element of the array.
# If x matches with an element, return the index.
# If x doesn’t match with any of the elements, return -1.

def linear_search(arr, x):
 
  for i in range(len(arr)):
    if arr[i] == x:
      return i
 
  return -1

myArray = [2, 5, 62, 665, 42, 52, 48, 7]

print(linear_search(myArray, 42))
# index 4

# Time Complexity: O(n)
# Space Complexity: O(1)
# We will come back to what this means...


# You could also use the 'in' operator
if 42 in myArray:
  print(myArray.index(42))

