import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 40)
y = np.sqrt(1 - (x**2))
plt.plot(x, y)
plt.xlabel("theta")
plt.ylabel("y")
plt.show()