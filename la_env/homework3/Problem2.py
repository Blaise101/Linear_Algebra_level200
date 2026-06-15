import numpy as np
import matplotlib.pyplot as plt
# from shortcuts import * # Optional, standard matplotlib 3D setup below handles it

# Setup the 3D plotting environment
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Define a range of values for our free variable parameter (t)
t = np.linspace(-10, 10, 100)

# --- Problem 2(a): Homogeneous Line ---
# Equation: x = t * [1, 1, 1]
x_a = 1 * t
y_a = 1 * t
z_a = 1 * t

# --- Problem 2(b): Non-Homogeneous Line ---
# Equation: x = [7, -1, 0] + t * [1, 1, 1]
x_b = 7 + 1 * t
y_b = -1 + 1 * t
z_b = 0 + 1 * t

# Plot the lines
ax.plot(x_a, y_a, z_a, label='Part (a): Homogeneous System (Through Origin)', color='blue', linewidth=2)
ax.plot(x_b, y_b, z_b, label='Part (b): Non-Homogeneous System (Shifted)', color='red', linewidth=2, linestyle='--')

# Plot the origin (0, 0, 0) for reference
ax.scatter(0, 0, 0, color='black', s=50, label='Origin (0,0,0)')

# Plot the translation point p = [7, -1, 0]
ax.scatter(7, -1, 0, color='darkred', s=50, label='Translation Point (7, -1, 0)')

# Setting labels and title
ax.set_xlabel('X1 Axis')
ax.set_ylabel('X2 Axis')
ax.set_zlabel('X3 Axis')
ax.set_title('Geometric Comparison of Problem 2 Solution Sets')

# Adjust view angle to clearly see they are parallel lines
# ax.view_init(elev=20, azim=45)

ax.legend()
plt.grid(True)
plt.show()