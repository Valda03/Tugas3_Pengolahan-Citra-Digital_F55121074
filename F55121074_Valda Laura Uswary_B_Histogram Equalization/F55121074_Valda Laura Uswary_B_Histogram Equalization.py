import cv2
import numpy as np
from matplotlib import pyplot as plt

# membaca citra
img = cv2.imread('HE.jpg', 0)

# membuat histogram
hist, bins = np.histogram(img.flatten(), 256, [0, 256])

# menampilkan histogram sebelum perbaikan
plt.hist(img.flatten(), 256, [0, 256])
plt.xlim([0, 256])
plt.show()

# melakukan ekualisasi histogram
eq_img = cv2.equalizeHist(img)

# membuat histogram setelah perbaikan
hist_result, bins_result = np.histogram(eq_img.flatten(), 256, [0, 256])

# menampilkan histogram setelah perbaikan
plt.hist(eq_img.flatten(), 256, [0, 256])
plt.xlim([0, 256])
plt.show()

# menampilkan citra asli dan hasil perbaikan
cv2.imshow('Gambar Original', img)
cv2.imshow('Gambar Equalized', eq_img)

cv2.waitKey(0)
cv2.destroyAllWindows()