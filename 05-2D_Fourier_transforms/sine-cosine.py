import numpy as np
import matplotlib.pyplot as plt

# Close all plot
plt.close('all')

# Give range to plot from 0 to 4pi
x = np.arange(0, 4*np.pi, 0.1)

# First Sine function
y1 = np.sin(x)
# Second Cosine function
y2 = np.cos(x)
# Shift 90 degree
y3 = np.sin((np.pi/2)-x)

# Three subplots sharing both x/y axes
f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
ax1.plot(x, y1, color='b')
ax1.set_title('Sin function', fontsize=18)
ax2.plot(x, y2, color='g')
ax2.set_title('Cos function', fontsize=18)
ax3.plot(x, y3, color='r')
ax3.set_title('Shift Sin function 90 degree', fontsize=18)

# You must call plt.show() to make graphics appear
plt.show()