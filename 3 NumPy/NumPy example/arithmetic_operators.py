import numpy as np

miles = np.array([1, 2, 3])
kilometers = miles * 1.6
print('Kilometers:', kilometers)

# Add
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
addition = arr1 + arr2
print('Addition:', addition)

# Subtract
subtraction = arr1 - arr2
print('Subtraction:', subtraction)

# Multiply
multiplication = arr1 * arr2
print('Multiplication:', multiplication)

# Divide
division = arr1 / arr2
print('Division:', division)

# Dot product 1
data = np.array([1, 2, 3])
powers_of_ten = np.array([[1, 10], [100, 1000], [10000, 100000]])
dot_product_1 = data.dot(powers_of_ten)
print('Dot product 1:\n', dot_product_1)

# Dot product 2
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
dot_product_2 = np.dot(matrix1, matrix2)
print('Dot product 2:\n', dot_product_2)
