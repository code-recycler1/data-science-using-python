import numpy as np

arr = np.random.randint(1, 11, (3, 4))
print('Start array:\n', arr)

arr_reshaped = arr.reshape(4, 3)
print('Reshaped array:\n', arr_reshaped)

arr_flattened = arr.flatten()
arr_raveled = arr.ravel()
print('Flattened array:\n', arr_flattened)
print('Raveled array:\n', arr_raveled)
