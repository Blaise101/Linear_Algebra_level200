from matplotlib import pyplot as plt
import numpy as np

# hom
t = np.linspace(-5,5,100)
xh = -2*t
yh = t

plt.plot(xh, yh, 'r', label='Homogeneous solution set' )
plt.plot(xh+4, yh, 'g', label='Nonhomogeneous solution set' )

# vectors
plt.quiver(
  0,0, # Tail
  -2,1, # Direction
  angles = 'xy',
  scale_units = 'xy',
  scale = 1,
  label = 'Vector (-2,1)'
)
plt.quiver(
  0,0, # Tail
  4,0, # Direction
  angles = 'xy',
  scale_units = 'xy',
  scale = 1,
  label = 'Vector (4,0)'
)

plt.axhline()
plt.axvline()

plt.grid()
plt.legend()
plt.show()




