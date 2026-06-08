import sympy

A = sympy.Matrix([
    [8, 11, -6, -7, 13],
    [-7, -8, 5, 6, -9],
    [11, 7, -7, -9, -6],
    [-3, 4, 1, 8, 7]
])

rref_matrix = A.rref()

print("RREF of Matrix A:")
sympy.pprint(rref_matrix)