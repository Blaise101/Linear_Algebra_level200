import numpy as np
import matplotlib.pyplot as plt

# Plot formatting
def plot_format():
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.grid(True)
    plt.xlim(-12, 12)
    plt.ylim(-12, 12)

# 1. Boat coordinates
boat = np.array([
    [0, 5, 8, 10, 4, 6, 3, 3, 1, 1, -2, 0],
    [0, 0.5, 2.5, 3.5, 2, 3, 8, 3, 6, 2, 2, 0]
])

# 2. Define the transformation matrices
M_y_axis = np.array([[-1, 0],
                     [ 0, 1]])

M_y_neg_x = np.array([[ 0, -1],
                      [-1, 0]])

M_origin = np.array([[-1, 0],
                     [ 0, -1]])

# 3. Apply transformations
boat_y_axis = M_y_axis @ boat
boat_y_neg_x = M_y_neg_x @ boat
boat_origin = M_origin @ boat


# 4. Data for plotting
boats = [
    boat,
    boat_y_axis,
    boat_y_neg_x,
    boat_origin
]

titles = [
    "1. Original Boat",
    "2. Reflection through y-axis",
    "3. Reflection through y = -x",
    "4. Reflection through Origin"
]

plt.figure(figsize=(14, 8))

for i in range(len(boats)):
    plt.subplot(2, 2, i + 1)
    plt.plot(boats[i][0], boats[i][1], marker='o')
    plt.title(titles[i])
    plot_format()


# Adjust spacing and display the figure
plt.suptitle("Transformations of a Boat", fontsize=18)
plt.show()