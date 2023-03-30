import matplotlib.pyplot as plt
import numpy as np

meter = np.array([40, 55, 60, 73, 89, 100, 110])
az1_price = np.array([500, 710, 750, 890, 1100, 1500, 1600])
az2_price = np.array([700, 900, 990, 1200, 1550, 1800, 1900])
az3_price = np.array([1000, 1230, 1400, 1900, 2500, 3000, 3700])

plt.plot(meter, az1_price, label="apartment price in zone 1", color="red")
plt.plot(meter, az2_price, label="apartment price in zone 2", color="blue")
plt.plot(meter, az3_price, label="apartment price in zone 3", color="green")
plt.xlabel("meter")
plt.ylabel("apartment price")
plt.legend()
plt.show()
