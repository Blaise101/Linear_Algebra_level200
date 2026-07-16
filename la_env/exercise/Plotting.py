import numpy as np
import matplotlib.pyplot as plt

def plot_format():
  plt.grid(True)
  plt.axis('equal')
  plt.xlim(-1,8)
  plt.ylim(-2,10)

# House Coordinates
house = np.array([[0,4, 4, 2, 0, 0], [0, 0, 3, 5, 3, 0]])

# scaling
scale = np.array([[1.5, 0], [0, 1.5]])
scaledHouse = scale@house


# PPOTTING
# original
plt.subplot(1,2,1)
plt.plot(house[0], house[1], marker='o', label="Original Plot", color="#D3AC37")
plot_format()

# rescaling
plt.subplot(1,2,2)
plt.plot(scaledHouse[0], scaledHouse[1], marker='o', label="Rescaled Plot", color="blue")
plot_format()

plt.show()