import numpy as np 
import matplotlib.pyplot as plt 
import cv2 
import math 

# Read image 
im = cv2.imread('brain.png',0) 

# Add zeros padding with (-1)^x+y 
nim = np.zeros((2*im.shape[0], 2*im.shape[1]), dtype = im.dtype) 
bnim = np.zeros((2*im.shape[0], 2*im.shape[1]), dtype =  im.dtype)
for i in range(im.shape[0]):
    for k in range(im.shape[1]):
        nim[i][k] = im[i][k] 
        bnim[i][k] = ((-1)**(i+k))*im[i][k] 
        
# Apply fft 
FS= np.fft.fft2(bnim) 

# Create a filter to keep low frequency, example a dish image in frequency domain
filt = np.zeros((2*im.shape[0], 2*im.shape[1]), dtype = im.dtype) 
center = (im.shape[1], im.shape[0]) 
radius = 100 
cv2.circle(filt, center, radius, (255, 255, 255), -1) 

# Apply filter 
G = filt*FS

# Inverse 
gt = np.real(np.fft.ifftn(G)) 

# Multiple with (-1)** (i+k) back 
for i in range(gt.shape[0]): 
    for k in range(gt.shape[1]): 
        gt[i][k] = ((-1)**(i+k))*gt[i][k] 

# Crop to original size back 
final = np.zeros((im.shape[0], im.shape[1]), dtype = gt.dtype) 
for i in range(final.shape[0]):
    for k in range(final.shape[1]):
        final[i][k] = gt[i][k]

plt.subplot(241) 
plt.imshow(im, 'gray')
plt.title('Original Image', fontsize=20) 
plt.axis("off") 

plt.subplot(242) 
plt.imshow(nim, 'gray') 
plt.title('Zeros Padding Image', fontsize=20) 
plt.axis("off") 

plt.subplot(243) 
plt.imshow(bnim, 'gray') 
plt.title('(-1)^(x+y)', fontsize=20) 
plt.axis ("off") 

plt.subplot(244) 
plt.imshow(20*np.log(np.abs(FS)), 'gray') 
plt.title('FT', fontsize=20) 
plt.axis("off") 

plt.subplot (245) 
plt.imshow(filt, 'gray') 
plt.title ('Filter', fontsize=20) 
plt.axis("off") 

plt.subplot(246) 
plt.imshow(20*np.log(np.abs(G)+1), 'gray') 
plt.title('After Filtering', fontsize=20) 
plt.axis("off") 

plt.subplot(247) 
plt.imshow(gt, 'gray') 
plt.title('Inverse with (-1)^(x+y)', fontsize=20) 
plt.axis ("off") 

plt.subplot(248) 
plt.imshow(final, 'gray')
plt.title('Final Result', fontsize=20) 
plt.axis("off") 

plt.show()