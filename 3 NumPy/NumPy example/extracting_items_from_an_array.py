import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Array:\n', arr)

# Get element at row 2, column 1
print('Element row 2, col 1:', arr[2, 1])

# Get a slice of the array
print('Slice:\n', arr[1:4])

# Get a subarray
print('Subarray:\n', arr[:3, :2])
