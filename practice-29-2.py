import matplotlib.pyplot as plt
import numpy as np

read_t = np.array([10, 12.5, 13, 15, 17, 17.5, 19])
grade = np.array([7, 17, 15, 12, 18, 19, 20])

plt.plot(read_t, grade, marker="o", ms="5", mfc="blue", color="green")
plt.xlabel("reading time")
plt.ylabel("grade")
plt.show()
