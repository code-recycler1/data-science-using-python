import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Start array:\n', arr)

arr_new = arr[:3, :2]
arr_new[0, 0] = 10
print('New array:\n', arr_new)
print('Updated start array:\n', arr)

arr_copy = arr[:3, :2].copy()
arr_copy[0, 0] = 15
print('Copied array:\n', arr_copy)
print('Start array:\n', arr)
