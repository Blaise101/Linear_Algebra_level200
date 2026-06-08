from sympy import Matrix

heatEquation  = Matrix([[27.6,30.2,162], [3100,6400,23610], [250,360,1623]])

solution = heatEquation.rref()

print(solution)