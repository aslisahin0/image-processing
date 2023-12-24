import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    equalized_img = cv2.equalizeHist(img)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(equalized_img, cmap='gray')
    plt.title('Equalized Image')

    plt.show()

if __name__ == "__main__":
    
    image_path = "moon.png"
    histogram_equalization(image_path)
