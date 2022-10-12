import matplotlib.pyplot as plt
import numpy as np
import math
x = np.linspace(0, 1, 30)
x1 = np.linspace(-4,4,30)
x2, y3 = np.meshgrid(np.linspace(-5, 5,150), np.linspace(-3,3,150))
y1 = x**4 - 10*x**2+10
y2 = x**3 - 3*x
z = -20*np.exp(-0.2*np.sqrt(0.5*(x2**2+y3**2)))-np.exp(0.5*np.cos(2*math.pi*x2)+np.cos(2*math.pi*y3))+math.e+20
rand = np.random.RandomState(0)
size = 1000*rand.rand(30)
colors = rand.rand(30)

fig, ax = plt.subplots(figsize=(10,10))
ax1 = plt.subplot2grid((9, 3), (0, 0))
plt.plot(x1,y1,'r', label = 'y1')
plt.plot(x1,y2,'b', label = 'y2')
plt.title('grid1')
plt.xlabel('X')
plt.ylabel('Y')

ax2 = plt.subplot2grid((9, 3), (0, 1))
plt.plot(x, y2,'g') 

ax3 = plt.subplot2grid((9, 3), (0, 2))
plt.plot(x, y1,'c') 

ax4 = plt.subplot2grid((9, 3), (1, 0),rowspan = 3, colspan = 3)
co = ax4.contourf(x2, y3, z, levels = 120)

ax5 = plt.subplot2grid((9, 2), (4, 0))
plt.plot(x, y2) 

ax6 = plt.subplot2grid((9, 2), (4, 1))
plt.plot(x, y1) 

ax7 = plt.subplot2grid((9, 2), (5, 0))
plt.plot(x, y2) 

ax8 = plt.subplot2grid((9, 2), (5, 1), rowspan = 2)
ax8.scatter(x,y2,s = size,c = colors, cmap = 'viridis', alpha = 0.4)

ax9 = plt.subplot2grid((9, 2), (6, 0))
plt.plot(x, y2,'r') 

ax10 = plt.subplot2grid((9, 1), (7, 0),rowspan = 3)
plt.plot(x, y1,'k') 
plt.plot(x, y2,'c') 
plt.show()