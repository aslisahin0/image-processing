import random 
import cv2 

def saltPepperNoise(img): 

	
	row , col = img.shape 
	number_of_pixels = random.randint(300, 10000) 
	for i in range(number_of_pixels): 
			
		y_coord=random.randint(0, row - 1) 
		x_coord=random.randint(0, col - 1) 
		img[y_coord][x_coord] = 255
		
	number_of_pixels = random.randint(300 , 10000) 
	for i in range(number_of_pixels): 
		
		y_coord=random.randint(0, row - 1) 
		x_coord=random.randint(0, col - 1) 
		img[y_coord][x_coord] = 0
		
	return img 

img = cv2.imread('lena.jpg', 
				cv2.IMREAD_GRAYSCALE) 

cv2.imwrite('salt-and-pepper-lena.jpg', 
			saltPepperNoise(img)) 
