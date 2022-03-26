import numpy as np
import matplotlib.pyplot as plt 
import cv2 

# Read Original Image 
orig = cv2.imread('catcat.jpg',0) 

# Apply fft2 to transform pixel domain to frequency domain 
FS = np.fft.fft2(orig) 

# Apply fftshift to shift low frequency in center and 
# high frequency is outside 
fshift = np.fft.fftshift(FS) 

magnitude_spectrum1 = 20*np.log(np.abs(fshift)) 

# Adding periodic noise to image in frequency domain 
# This is just and example of adding noise 
# In Real application, image is contained noise from environment (eg. camera) 

# Define the size of fshift 
m, n = fshift.shape 

# Define the cen 
cx = int(n/2) 
cy = int(m/2) 

# Generate the Theta (angle) goes from 0 to 2pi 
theta = np.linspace(0, 2*np.pi, 9) 

# Define radius of the circle 
r = 80 

# Compute x and y coordinate of circle 
x = (r*np.cos(theta) + cx) 
y = (r*np.sin(theta) + cy) 

# Convert to integer of array 
x = x.astype(int)
y = y.astype(int)

# Add this noise to fshift by looking at coordinate of noise 
# Then replace frequency of fshift to some value 
# This example we give the new value equal to DC component of fshift 
# divide by 2 
for i, j in zip(x, y) :
    fshift[j,i] = (np.abs(fshift[cy, cx])/2) + 0j 

magnitude_spectrum2 = 20*np.log(np.abs(fshift)) 

# Transform to pixel domain back 
f_ishift = np.fft.ifftshift(fshift) 
img_back = np.fft.ifft2(f_ishift) 

img_back = np.abs(img_back)

plt.subplot(231) 
plt.imshow(orig, 'gray') 
plt.title('Original Image', fontsize=20) 
plt.axis ("off") 

plt.subplot(232) 
plt.imshow(magnitude_spectrum1, 'gray') 
plt.title('FFT_Original', fontsize=20) 
plt.axis("off") 

plt.subplot(233) 
plt.plot(x, y, 'o') 
plt.title('Periodic Noise', fontsize=20) 
plt.axis("off") 

plt.subplot(234) 
plt.imshow(magnitude_spectrum2, 'gray') 
plt.title('Adding Noise', fontsize=20) 
plt.axis("off") 

plt.subplot(235) 
plt.imshow(img_back, 'gray') 
plt.title('NoisyImage', fontsize=20) 
plt.axis("off") 

plt.show()