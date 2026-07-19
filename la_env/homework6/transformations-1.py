import numpy as np
import matplotlib.pyplot as plt

# Plot formatting
def plot_format():
    plt.grid(True)
    plt.xlim(-4, 12)
    plt.ylim(-7, 10)

# House coordinates

house = np.array([
    [0, 4, 4, 2, 0, 0],
    [0, 0, 3, 5, 3, 0]
])

# Transformation matrices

# Scaling
S = np.array([
    [1.5, 0],
    [0, 1.5]
])

# Rotation by 45 degrees
theta = np.radians(45)
R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

# Horizontal shear
k = 0.8
H = np.array([
    [1, k],
    [0, 1]
])

# Vertical shear
V = np.array([
    [1, 0],
    [k, 1]
])

# Reflection through x-axis
F = np.array([
    [1, 0],
    [0, -1]
])

# Apply transformations

scaled = S @ house
rotated = R @ house
horizontal = H @ house
vertical = V @ house
reflected = F @ house

# Data for plotting

houses = [
    house,
    scaled,
    rotated,
    horizontal,
    vertical,
    reflected
]

titles = [
    "Original",
    "Rescaling",
    "Rotation",
    "H. Shear",
    "V. Shear",
    "Reflection"
]

# Plotting

plt.figure(figsize=(14, 8))

for i in range(len(houses)):
    plt.subplot(2, 3, i + 1)
    plt.plot(houses[i][0], houses[i][1], marker='o')
    plt.title(titles[i])
    plot_format()

plt.suptitle("Transformations of a House", fontsize=18)

plt.show()
