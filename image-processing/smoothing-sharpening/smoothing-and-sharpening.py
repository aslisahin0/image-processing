import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
   
    image_path = 'input.png'
    original_image = cv2.imread(image_path)

    smoothed_image = cv2.GaussianBlur(original_image.copy(), (5, 5), 0)

    kernel_sharpening = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened_image = cv2.filter2D(original_image.copy(), -1, kernel_sharpening)

    original_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    smoothed_rgb = cv2.cvtColor(smoothed_image, cv2.COLOR_BGR2RGB)
    sharpened_rgb = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB)

 
    aspect_ratio = original_image.shape[1] / original_image.shape[0]

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    for ax in axes:
        ax.set_aspect(aspect_ratio)

    axes[0].imshow(original_rgb)
    axes[0].set_title('Original Image')
    axes[0].axis('on')
    axes[0].set_facecolor('black')

    axes[1].imshow(smoothed_rgb)
    axes[1].set_title('Smoothed Image')
    axes[1].axis('on')
    axes[1].set_facecolor('black')

    axes[2].imshow(sharpened_rgb)
    axes[2].set_title('Sharpened Image')
    axes[2].axis('on')
    axes[2].set_facecolor('black')

    plt.show()

if __name__ == "__main__":
    main()
