import matplotlib.pyplot as plt
import numpy as np

sports = np.array(['Soccer', 'Swimming', 'Hockey', 'Basketball'])
number_of_students = np.array([120, 80, 150, 200])

# Sort the data for better visualization
number_of_students, sports = zip(*sorted(list(zip(number_of_students, sports))))

plt.pie(number_of_students, labels=sports, autopct='%1.1f%%', startangle=90)
plt.show()
