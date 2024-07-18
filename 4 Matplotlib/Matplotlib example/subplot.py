import matplotlib.pyplot as plt

# Example data
a = [0, 1, 2, 3, 4]
b = [4, 4, 0, 3, 0]
c = [3, 2, 1, 0, 4]
d = [3, 2, 2, 3, 3]
e = [1, 4, 4, 0, 2]

plt.subplot(2, 2, 1)
plt.ylim(0, 5)
plt.plot(a, b, 'b')
plt.title('Plot 1: a vs b')

plt.subplot(2, 2, 2)
plt.ylim(0, 5)
plt.plot(a, d, 'g')
plt.title('Plot 2: a vs d')

plt.subplot(2, 2, 3)
plt.ylim(0, 5)
plt.plot(a, c, 'r')
plt.title('Plot 3: a vs c')

plt.subplot(2, 2, 4)
plt.ylim(0, 5)
plt.plot(a, e, 'y')
plt.title('Plot 4: a vs e')

plt.tight_layout()
plt.show()
