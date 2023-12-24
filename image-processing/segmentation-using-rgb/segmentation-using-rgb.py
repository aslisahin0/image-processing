import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2gray

img = imread('input.webp')[:, :, :3]
img_gs_1c = rgb2gray(img)

fig, ax = plt.subplots(1, 1, figsize=(8, 8))
ax.set_title("Original Image")
ax.imshow(img)
ax.set_axis_off()
plt.show()

img_gs = ((np.stack([img_gs_1c] * 3, axis=-1) * 255)
          .astype('int').clip(0, 255))

red_mask = ((img[:, :, 0] > 150) &
            (img[:, :, 1] < 100) &
            (img[:, :, 2] < 200))
img_red = img_gs.copy()
img_red[red_mask] = img[red_mask]

green_mask = ((img[:, :, 0] < 190) &
              (img[:, :, 1] > 190) &
              (img[:, :, 2] < 190))
img_green = img_gs.copy()
img_green[green_mask] = img[green_mask]

blue_mask = ((img[:, :, 0] < 80) &
             (img[:, :, 1] < 85) &
             (img[:, :, 2] > 50))
img_blue = img_gs.copy()
img_blue[blue_mask] = img[blue_mask]

fig, ax = plt.subplots(1, 3, figsize=(21, 7))
ax[0].set_title("Red Segment")
ax[0].imshow(img_red)
ax[0].set_axis_off()
ax[1].set_title("Green Segment")
ax[1].imshow(img_green)
ax[1].set_axis_off()
ax[2].set_title("Blue Segment")
ax[2].imshow(img_blue)
ax[2].set_axis_off()
plt.show()
