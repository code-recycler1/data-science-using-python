import numpy as np

arr = np.random.randint(1, 11, (3, 5))
print(arr)

print('Num Dimensions:', arr.ndim)
print('Shape:', arr.shape)
print('Number of rows:', arr.shape[0])
print('Number of columns:', arr.shape[1])
print('Datatype:', arr.dtype)
print('Size:', arr.size)
