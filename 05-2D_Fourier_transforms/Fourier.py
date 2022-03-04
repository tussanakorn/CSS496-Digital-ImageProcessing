import numpy as np
import matplotlib.pyplot as plt

# Close all plot
plt.close('all') 

# Initialize parameter 
w = np.pi/2 
a = 0 
signal = [] 
scale = 0.0001 

# Give range of time from -4pi to 4pi 
t = np.arange (-4*np.pi, 4*np.pi, scale) 

# Compute function f
for i in np.nditer(t):
    a = a + 1 
    if (i>= -w/2) and (i<=w/2): 
        y = 1 
    else: 
        y = 0 
    signal.append(y) 

x = np.array(signal) 

# Theorical 
f_theory = 1/t 
Y_theory = (w/ (np.pi*w*f_theory)) *np.sin(np.pi*w*f_theory) 

# Simulation 
dt = t[1]-t [0] # time different 
Y_simulation = np.fft.fft (x) 
f_simulation = np.fft.fftfreq(x.size, d=dt)

fig = plt.figure(1, figsize= (10,8), frameon=False)
ax1 = fig.add_subplot(131)
ax1.plot(t, x) 
ax1.set_xlabel('t', fontsize=18) 
ax1.set_ylabel('x(t)', fontsize=18) 
ax1.set_title ('Original Signal', fontsize=24) 
ax1.set_xlim(-10,10) # adjust the max leaving min unchanged 

ax2 = fig.add_subplot(132) 
ax2.plot(f_theory, np.abs(Y_theory), color='g') 
ax2.set_xlabel('freq', fontsize=18) 
ax2.set_ylabel('Theory_Absolute Y(f)', fontsize=18) 
ax2.set_xlim (-5,5) # adjust the max leaving min unchanged 
ax2.set_title('Theory', fontsize=24) 

ax3 = fig.add_subplot(133) 
ax3.plot(f_simulation, np.abs (np.real(Y_simulation) *scale), color='r') 
ax3.set_xlabel ('freq', fontsize=18) 
ax3.set_ylabel ('Simulation Absolute Y(f)', fontsize=18)
ax3.set_xlim (-5,5) # adjust the max leaving min unchanged 
ax3.set_title ('Simulation', fontsize=24) 

plt.show()
