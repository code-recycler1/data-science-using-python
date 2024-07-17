import numpy as np

prices = np.array([187.00, 220.00, 228.00, 258.00, 260.00, 280.00, 294.00, 298.00, 314.00, 4860.00])
print(np.percentile(prices, [25, 50, 75]))
print('90% of the room prices are lower than', round(np.percentile(prices, 90), 2), '$')
