import numpy as np

# Create a 1D array from a list
list1 = [0, 1, 2, 3, 4]
arr1d = np.array(list1)

# Create a 2D array from a list of lists and datatype float
list2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
arr2d_float = np.array(list2, dtype='float')

# Other np methods
arr_ones = np.ones((3, 2))
arr_zeros = np.zeros((3, 3))
arr_random = np.random.random((4, 3))
arr_full = np.full((4, 4), 6)

# Create a 1D array from a sequence of numbers
arr_sequence_1 = np.arange(5)
arr_sequence_2 = np.arange(7, 15)

print('1D\n', arr1d)
print('2D\n', arr2d_float)
print('Ones\n', arr_ones)
print('Zeros\n', arr_zeros)
print('Random\n', arr_random)
print('Full\n', arr_full)
print('Arange 1\n', arr_sequence_1)
print('Arange 2\n', arr_sequence_2)
