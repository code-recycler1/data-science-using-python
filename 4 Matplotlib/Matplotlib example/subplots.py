import matplotlib.pyplot as plt

# Example data
a = [0, 1, 2, 3, 4]
b = [1, 3, 0, 1, 3]
c = [0, 1, 4, 0, 4]
d = [3, 0, 0, 0, 1]
e = [0, 1, 2, 3, 1]

fig, axs = plt.subplots(2, 2, sharey=True)

axs[0, 0].plot(a, b, 'b')
axs[0, 1].plot(a, c, 'g')
axs[1, 0].plot(a, d, 'r')
axs[1, 1].plot(a, e, 'y')

plt.show()
