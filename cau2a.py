import matplotlib.pyplot as plt
import numpy as np
import math
x, y = np.meshgrid(np.linspace(-5, 5,550), np.linspace(-5,5,550))
z = -20*np.exp(-0.2*np.sqrt(0.5*(x**2+y**2)))-np.exp(0.5*np.cos(2*math.pi*x)+np.cos(2*math.pi*y))+math.e+20
fig, ax = plt.subplots(figsize = (11,9))
ax.plot(0,0,'ro',markersize=3)
co = ax.contourf(x, y, z, levels=120)
co2 = ax.contour(x, y, z,colors = 'white', linewidths = 0.5, linestyles = 'solid',levels = 10)
plt.colorbar(co)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Câu 2 a')
plt.show()