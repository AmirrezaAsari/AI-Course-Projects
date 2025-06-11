import numpy as np
import matplotlib.pyplot as plt

def objective(x, y):
    value = 2 + (x**2 - (np.cos(2 * x * np.pi))) + (y**2 - (np.cos(2 * y * np.pi)))
    return value

x = np.linspace(-1.6, 1.6, 120)
y = np.linspace(-1.6, 1.6, 120)
X, Y = np.meshgrid(x, y)
Z = objective(X, Y)

# Clip Z-values to [0, 9]
Z_clipped = np.clip(Z, 0, 9)

# Plot with adjusted range
plt.figure(figsize=(10, 6))
contour = plt.contourf(X, Y, Z_clipped, levels=50, cmap='jet', vmin=0, vmax=9)
plt.colorbar(contour, label='')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Contour Plot')
plt.show()

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot clipped surface
surf = ax.plot_surface(X, Y, Z_clipped, cmap='jet', edgecolor='none', vmin=0, vmax=9)
fig.colorbar(surf, label='')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('3D Plot')
plt.show()