import numpy as np

arr = np.array([1, 4, 2, 7, 9, 3, 5, 8])
indexes_to_keep = np.where(arr > 5)
arr_filtered = arr[indexes_to_keep]
print(arr_filtered)

# With additional parameters
arr_filtered = np.where(arr > 5, arr, 0)
print(arr_filtered)
