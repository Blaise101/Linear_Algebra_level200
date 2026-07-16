import numpy as np
import matplotlib.pyplot as plt

def plot_format():
  plt.grid(True)
  plt.axis('equal')
  plt.xlim(-5,8)
  plt.ylim(-5,10)

# House Coordinates
house = np.array([[0,4, 4, 2, 0, 0], [0, 0, 3, 5, 3, 0]])

# TRANSFORMATION MATRICES

# scaling
scale = np.array([[1.5, 0], [0, 1.5]])

# Rotation through 45 degrees
theta = np.radians(45)
rotation = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

# Horizontal shear
k=0.7
horizontal = np.array([[1, k], [0, 1]])

# Vertical shear
k=0.7
vertical = np.array([[1, 0], [k, 1]])

# Reflection through the x-axis
reflection = np.array([[1, 0], [0, -1]])

# TRANSFORMED HOUSES
scaledHouse = scale@house
verticalHouse = vertical@house
horizontalHouse = horizontal@house
reflectedHouse = reflection@house
rotatedHouse = rotation@house

# PLOTTING

# original
plt.subplot(2,3,1)
plt.plot(house[0], house[1], marker='o', color="#D3AC37")
plt.title('Original Plot')
plot_format()

# rescaling
plt.subplot(2,3,2)
plt.plot(scaledHouse[0], scaledHouse[1], marker='o', color="#378467")
plt.title("Scaled Matrix")
plot_format()

# vertical
plt.subplot(2,3,3)
plt.plot(verticalHouse[0], verticalHouse[1], marker='o', color="#745C53")
plt.title("Vertical Matrix")
plot_format()

# horizontal
plt.subplot(2,3,4)
plt.plot(horizontalHouse[0], horizontalHouse[1], marker='o', color="#324984")
plt.title("Horizontal Matrix")
plot_format()

# reflected
plt.subplot(2,3,5)
plt.plot(reflectedHouse[0], reflectedHouse[1], marker='o', color="#abbc36")
plt.title("Reflected Matrix")
plot_format()

# rotated
plt.subplot(2,3,6)
plt.plot(rotatedHouse[0], rotatedHouse[1], marker='o', color="#112234")
plt.title("Rotated Matrix")
plot_format()



plt.show()