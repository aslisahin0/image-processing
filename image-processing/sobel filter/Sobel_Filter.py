import cv2
import numpy as np
from matplotlib import pyplot as plt

img0 = cv2.imread('input.jpg')

gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

img = cv2.GaussianBlur(gray, (3, 3), 0)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)  
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)  

plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 2), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 3), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()
