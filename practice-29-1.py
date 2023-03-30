import matplotlib.pyplot as plt
import numpy as np

temp = np.array([20, 100, 250, 400, 420, 440, 510])
pressure = np.array([120, 300, 700, 1000, 1100, 1500, 2000])

plt.plot(temp, pressure, marker="o", ms="5", linestyle="-.", color="#4b0082")
plt.xlabel("temperature")
plt.ylabel("pressure")
plt.show()
