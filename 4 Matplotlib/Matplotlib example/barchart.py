import matplotlib.pyplot as plt
import numpy as np

groups = np.array(['2IT01', '2IT02', '2IT03', '2IT04', '2IT05'])
number_of_men = np.array([20, 35, 30, 35, 27])

plt.bar(groups, number_of_men)
plt.title('Number of Male Students per Group')
plt.show()
