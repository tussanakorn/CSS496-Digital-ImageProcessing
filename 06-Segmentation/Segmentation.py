import cv2
import numpy as np

img = cv2.imread('brain.png',0)

# Define the mask (kernel)
kernel = np.array(([-1,-1,-1],
                   [ 0, 0, 0],
                   [ 1, 1, 1]), dtype='int')

# Apply convolution
output = cv2.filter2D(img, -1, kernel)

# Show multiple image in one imshow
numpy_horizontal = np.hstack((img, output))

cv2.imshow('Result', numpy_horizontal)
cv2.waitKey(0)