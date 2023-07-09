import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.decomposition import PCA

image = mpimg.imread("Practice-54-img.png")
m, n, c = image.shape

plt.imshow(image)
plt.show()

img_r = np.reshape(image, (m, n * c))
print(img_r)

min0 = min(m, n)

def plot_img_k(k):
    pca = PCA(n_components=k).fit(img_r)
    img_c = pca.transform(img_r)
    img_cr = pca.inverse_transform(img_c)
    plt.imshow(img_cr)

k_lst = [2, 10, 25, 50, 100, 125]

for i in range(len(k_lst)):
    plt.subplot(2, 3, i + 1)
    plot_img_k(k_lst[i])
    plt.title("components: " + str(k_lst[i]))

plt.show()

for i in range(50):
    ipca = PCA(n_components=i)
    img_c = ipca.fit_transform(img_r)
    img_cr = ipca.inverse_transform(img_c)
    variance_exp_cumsum = ipca.explained_variance_ratio_.cumsum()
plt.plot(range(1, 50), variance_exp_cumsum)
plt.xlabel("n_component")
plt.ylabel("variance_sum")
plt.show()

