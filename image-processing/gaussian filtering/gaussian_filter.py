import cv2
import numpy as np

def apply_gaussian_blur(image_path, kernel_size):
    img = cv2.imread(image_path)

    blurred_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

    cv2.imshow('Original Image', img)
    cv2.imshow('Gaussian Blur', blurred_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    
    image_path = "lena.jpg"
    kernel_size = 5
    apply_gaussian_blur(image_path, kernel_size)
