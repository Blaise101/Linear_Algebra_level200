import numpy as np

# Define matrix A and vector b
A = np.array([
    [27.6, 30.2],
    [3100, 6400],
    [250, 360]
])
b = np.array([162, 23610, 1623])

# Using least squares to solve the system safely
x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

print(f"Tons of Anthracite (x1): {x[0]:.2f}")
print(f"Tons of Bituminous (x2): {x[1]:.2f}")