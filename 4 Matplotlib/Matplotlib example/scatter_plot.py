import matplotlib.pyplot as plt
import numpy as np

hours_studied = np.array([16, 6, 20, 8, 25, 12, 10, 8, 5, 18])
grades = np.array([12, 7, 14, 6, 14, 13, 9, 6, 6, 16])

plt.scatter(hours_studied, grades)
plt.xticks(np.arange(0, 26, step=2))
plt.yticks(np.arange(0, 20, step=5))
plt.xlabel('Hours Studied')
plt.ylabel('Final Grade')
plt.show()
