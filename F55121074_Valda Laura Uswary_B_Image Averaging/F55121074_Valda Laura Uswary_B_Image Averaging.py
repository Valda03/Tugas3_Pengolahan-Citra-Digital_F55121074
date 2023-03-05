import cv2
import numpy as np

# membaca citra asli
img = cv2.imread('IA.jpg', 0)

# mengatur ukuran kernel filter
kernel_size = 3

# mengatur variasi deviasi standard pada noise Gaussian
deviations = [16, 32, 64, 128]

# melakukan filter rata-rata pada masing-masing citra bernoise
for dev in deviations:

    # menambahkan noise Gaussian pada citra asli
    noise = np.random.normal(0, dev, size=img.shape)
    noisy_img = np.clip(img + noise, 0, 255).astype(np.uint8)

    # membuat kernel filter rata-rata
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size**2)

    # menampilkan citra asli, citra yang diberi noise, dan citra hasil filter
    cv2.imshow('Original Image', img)
    cv2.imshow(f'Noisy Image (dev={dev})', noisy_img)

cv2.waitKey(0)
cv2.destroyAllWindows()