import sympy as sp

"""
Solve a nonhomogeneous linear system using SymPy.

Question:
    x + 2y = 4
    2x + 4y = 8

Method 1: Solve the equations directly using linsolve.
Method 2: Solve the matrix equation A*x = b using linsolve.
"""

# method 1
x,y = sp.symbols('x, y')
solution = sp.linsolve([x+2*y-4, 2*x+4*y-8], x,y)
print(solution)

# method 2
A = sp.Matrix([[1,2], [2,4]])
b = sp.Matrix([4,8])
solution = sp.linsolve((A,b), x,y)
print(solution)

import numpy as np
from matplotlib import pyplot as plt

print(np.linspace(-1,1,20))
x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)
plt.plot(y)
plt.show()