import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.025)
y = np.arange(-2, 2, 0.025)

X, Y = np.meshgrid(x, y)
z1 = np.exp(-X ** 2 - Y ** 2)
z2 = np.exp(- (X-1) ** 2 - (Y - 1) ** 2)
Z = (z1 - z2) ** 2
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_surface(X, Y, Z)
plt.show()