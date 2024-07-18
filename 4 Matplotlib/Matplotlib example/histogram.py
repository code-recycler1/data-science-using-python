import matplotlib.pyplot as plt
import numpy as np

results = np.random.randint(1, 21, (100, 1))  # 100 students' exam results
intervals = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  # Bins

plt.hist(results, bins=intervals, ec='black')
plt.xticks(intervals)
plt.yticks(np.arange(0, 20, step=2))
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.show()
