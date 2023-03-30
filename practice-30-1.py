import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(np.pi / 2, (3 * np.pi) / 2, 100)
y = 1 - (np.cos(x))**2
plt.plot(x, y)
plt.xlabel("theta")
plt.ylabel("y")
plt.show()