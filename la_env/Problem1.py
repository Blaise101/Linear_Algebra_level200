from sympy import Matrix

myMatrix = Matrix([[20, 30, 150], [550, 500, 2825]])

solution = myMatrix.rref()

print(solution)