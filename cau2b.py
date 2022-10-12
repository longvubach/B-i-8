import matplotlib.pyplot as plt
import numpy as np
import math
x, y = np.meshgrid(np.linspace(-10, 10,500), np.linspace(10, -10,500))
z = -abs(np.sin(x)*np.cos(y)*np.exp(abs(1-(np.sqrt(x**2+y**2))/math.pi)))
fig, ax = plt.subplots(figsize = (11,9))
co = ax.contourf(x, y, z,levels=100)
co2 = ax.contour(x, y, z,colors = 'white', linewidths = 0.5, linestyles = 'solid')
ax.plot(8.05502,9.66459,'ro',markersize=3)
ax.plot(-8.05502,9.66459,'ro',markersize=3)
ax.plot(8.05502,-9.66459,'ro',markersize=3)
ax.plot(-8.05502,-9.66459,'ro',markersize=3)
fig.colorbar(co)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Câu 2 b')
plt.show()