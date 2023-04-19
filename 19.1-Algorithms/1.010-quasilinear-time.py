# O(n log n) - Quasilinear Time. 
# Also called log-linear complexity or even... “linearithmic”...

# An algorithm is said to have a quasilinear time complexity when each operation on the input data has itself a logarithm time complexity.
# It is commonly seen in sorting algorithms such as mergesort, timsort and heapsort, though these are not mentioned on your syllabus 

# For example: 
# for each value in the data1 (O(n)) use the binary search (O(log n)) to search the same value in data2.

# for value in data1:
    # result.append(binary_search(data2, value))


def binary_search(list, item):
  low = 0
  high = len(list) - 1

  while low <= high:
    mid = (low + high) // 2 
    guess = list[mid]

    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1

  return None

data1 = [14, 14, 3, 10, 11, 9, 19]
data2 = [3, 9, 10, 11, 12, 13, 14, 17, 18, 19] # sorted
result = []

for value in data1:
    result.append(binary_search(data2, value))

print(result)