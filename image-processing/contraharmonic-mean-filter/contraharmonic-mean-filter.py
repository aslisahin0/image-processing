import cv2
import numpy as np

def contraharmonic_mean_filter(image, window_size, Q):
   
    padded_image = cv2.copyMakeBorder(image, window_size // 2, window_size // 2, window_size // 2, window_size // 2, cv2.BORDER_CONSTANT)
    
    filtered_image = np.zeros_like(image, dtype=np.float64)

    for i in range(window_size // 2, padded_image.shape[0] - window_size // 2):
        for j in range(window_size // 2, padded_image.shape[1] - window_size // 2):
            window = padded_image[i - window_size // 2:i + window_size // 2 + 1, j - window_size // 2:j + window_size // 2 + 1]

            numerator = np.sum(np.power(window, Q + 1))
            denominator = np.sum(np.power(window, Q))

            if denominator != 0:
                filtered_image[i - window_size // 2, j - window_size // 2] = numerator / denominator

    filtered_image = np.uint8(filtered_image)
    
    return filtered_image

img = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

filtered_img = contraharmonic_mean_filter(img, window_size=3, Q=1.5)

cv2.imshow('Before', img)
cv2.imshow('After', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
