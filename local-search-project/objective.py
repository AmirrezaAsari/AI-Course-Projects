import numpy as np
import matplotlib.pyplot as plt

def objective(x, y):
    value = 3*(1-x)**2*np.exp(-x**2 - (y+1)**2) - 10*(x/5 - x**3 - y**5)*np.exp(-x**2 - y**2) -1/3*np.exp(-(x+1)**2 - y**2)
    return value

x = np.linspace(-2.5, 2.5, 100)
y = np.linspace(-2.5, 2.5, 100)
X, Y = np.meshgrid(x, y)
Z = objective(X, Y)

# Clip Z-values to [-8, 8]
Z_clipped = np.clip(Z, -8, 8)

# Plot with adjusted range
plt.figure(figsize=(10, 6))
contour = plt.contourf(X, Y, Z_clipped, levels=50, cmap='jet', vmin=-8, vmax=8)
plt.colorbar(contour, label='')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Contour Plot')
plt.show()

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot clipped surface
surf = ax.plot_surface(X, Y, Z_clipped, cmap='jet', edgecolor='none', vmin=-8, vmax=8)
fig.colorbar(surf, label='')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('3D Plot')
plt.show()