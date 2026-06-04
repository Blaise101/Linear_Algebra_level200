from sympy import Matrix

# My Matrix
b = Matrix([[1, 2], [3, 4]])
print(b)
print(b.shape)

# My Vector

v = Matrix([1, 2])
print(v)
print(v.shape)

new_matrix = Matrix([[1,-2,1], [0,2,-8], [5,0,-5]])
print(new_matrix)
print(new_matrix.shape)

# element in the first row and second column
print(new_matrix[0, 1])

# or
print(new_matrix[1])

# show first row
print(new_matrix.row(0))

# echelon form
print(new_matrix.echelon_form())

print(new_matrix.rref()) # reduced row echelon form