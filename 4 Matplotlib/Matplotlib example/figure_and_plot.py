import matplotlib.pyplot as plt
import numpy as np

average_monthly_temperatures_year1 = np.array([5.3, 8.1, 10.5, 14.6, 18.3, 22.1, 25.6, 24.4, 20.3, 15.2, 10.8, 6.4])
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

fig = plt.figure(figsize=(10, 4))  # width=10, height=4
plt.plot(months, average_monthly_temperatures_year1)
plt.title("Average Monthly Temperatures")
plt.xlabel("Months")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()
