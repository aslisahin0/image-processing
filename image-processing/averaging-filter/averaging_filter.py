import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('input.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original')

blurred_img = cv2.blur(img, (3, 3))

plt.subplot(1, 2, 2)
plt.imshow(blurred_img)
plt.title('Averaging')

plt.show()