import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])

print("Mean value is: ", arr1.mean())
print("Median value is: ", np.median(arr1))
print("Standard deviation is: ", arr1.std())
print("Max value is: ", arr1.max())
print("Min value is: ", arr1.min())

arr2 = np.random.randint(1, 11, (3, 4))
print('Array 2:\n', arr2)
print("Min per column", arr2.min(axis=0))
print("Min per row", arr2.min(axis=1))
