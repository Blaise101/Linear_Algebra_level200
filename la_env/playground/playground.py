from sympy import Matrix

A  = Matrix([[4,-2,5,-5,7],
             [-9,7,-8,0,5],
             [-6,4,5,3,9],
             [5,-3,8,-4,7]])

solution = A.rref()

print(solution)