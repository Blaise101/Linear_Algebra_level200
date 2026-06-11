import numpy as np
from matplotlib import pyplot as plt

y,z=np.meshgrid(np.linspace(-5,5), np.linspace(-5,5))  #y,z values

ax=plt.axes(projection='3d')

# hom
ax.plot_surface(-y-z,y,z, alpha=0.4)

# nonhom
ax.plot_surface(3-y-z,y,z, alpha=0.4)

ax.quiver(0,0,0, -1,1,0, color='black')
ax.quiver(0,0,0, 1,-1,1, color='black')

plt.show()