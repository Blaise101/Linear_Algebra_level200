import sympy as sp

A = sp.Matrix([
    [3,  4, -7, 0],
    [5, -8,  7, 4],
    [6, -8,  6, 4],
    [9, -7, -2, 0]
])
b = sp.Matrix([4, -4, -4, -7])

# Create augmented matrix [A | b]
augmented_matrix = A.row_join(b)

# Compute RREF
rref_matrix, pivot_columns = augmented_matrix.rref()

print("\nRREF of the augmented matrix:\n")
sp.pprint(rref_matrix)