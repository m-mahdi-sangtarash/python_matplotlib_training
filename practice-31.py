import matplotlib.pyplot as plt
import numpy as np

labels = ["physic", "chemistry", "math", "literature", "language", "andishe", "exercise"]
mahdi = [13, 19, 15, 17, 14, 14, 19]
arya = [19, 17, 15, 18, 18.5, 17, 18]

n = len(labels)
x = np.arange(n)

w = 0.2

plt.bar(x - w / 2, mahdi, width=w, color="blue", label="mahdi")
plt.bar(x + w / 2, arya, width=w, color="red", label="arya")
plt.xlabel("lessons")
plt.ylabel("grades")
plt.ylim(0, 20)
plt.grid()
plt.legend()
plt.show()