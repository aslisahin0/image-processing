import numpy as np
from skimage.draw import disk
import matplotlib.pyplot as plt
from skimage.morphology import opening, closing

shape = (25, 25)
selem_circ = np.array([[0, 1, 0],
                       [1, 1, 1],
                       [0, 1, 0]])

circ_img = np.zeros(shape, dtype=np.uint8)
rr, cc = disk((12, 12), 10, shape=shape)
circ_img[rr, cc] = 1

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(circ_img, cmap='gray')
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(selem_circ, cmap='gray')
plt.title("Structuring Element")

plt.show()

image_opening = opening(circ_img, selem_circ)

image_closing = closing(circ_img, selem_circ)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_opening, cmap='gray')
plt.title("Opening")

plt.subplot(1, 2, 2)
plt.imshow(image_closing, cmap='gray')
plt.title("Closing")

plt.show()
