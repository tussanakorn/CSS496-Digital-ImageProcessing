import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
# Close all plot 
plt.close('all') 

# Initialize parameter 
resx = 120 
resy = 120 
cx = resx/2 
cy=resy/2 

fxy = [[0 for x in range (resx)] for y in range (resy)] 

# Compute function f 
for i in range (resx): 
    for k in range (resy): 
        if (k>= (cx-10)) and (k<= (cx+10)) and (i>=(cy-5)) and (i<= (cy+5)): 
            fxy[i][k]=1 
        else: 
            fxy[i][k]=0 

FS = np.fft.fftn(fxy) 
fig = plt.figure(1, figsize=(10,8), frameon=False) 
ax1 = fig.add_subplot (131) 
ax1.imshow(fxy, cmap='gray') 
ax1.set_title('Original Image', fontsize=24) 

# Turn off tick labels 
ax1.set_yticklabels([]) 
ax1.set_xticklabels([])

ax2 = fig.add_subplot(132)

# Use fftshift to shift low frequency in the center 
ax2.imshow((np.abs(np.fft.fftshift(FS)))) 
ax2.set_title('FT', fontsize=24) 

# Turn off tick labels 
ax2.set_yticklabels([]) 
ax2.set_xticklabels([]) 

# Plot the surface 
ax3 = fig.add_subplot(133, projection='3d')
X = np.arange(0, 120, 1) 
Y = np.arange (0, 120, 1) 
X, Y = np.meshgrid (X, Y) 
surf = ax3.plot_surface (X, Y, (np.abs(np.fft.fftshift(FS))), cmap = 'seismic') 

plt.show()