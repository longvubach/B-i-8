import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-4,4,100)
y1 = x**4 - 10*x**2+10
y2 = x**3 - 3*x
fig, ax = plt.subplots(figsize = (10,7))
ax.plot(x,y1,'r', label = 'y1')
ax.plot(x,y2,'b', label = 'y2')
plt.title('Đồ thị câu 1')
plt.xlabel('X')
plt.ylabel('Y')
ax.legend()
q = np.argwhere(np.diff(np.sign(y2 - y1))).flatten()
ax.plot(x[q], y2[q], 'ks',markersize=10)
for i in range(len(q)):
    a = round(x[q[i]],1)
    b = round(y2[q[i]],1)
    plt.text(x[q[i]]-1,y2[q[i]]+10,(a,b))
ax.grid()
plt.show()