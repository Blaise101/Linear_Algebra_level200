import sympy as sp

"""
Solve a nonhomogeneous linear system using SymPy.

Question:
    x + y + z = 3
    2x + 2y + 2z = 6

Method 1: Solve the equations directly using linsolve.
Method 2: Solve the matrix equation A*x = b using linsolve.
"""

# Method 1

x,y,z = sp.symbols('x, y, z')
solution = sp.linsolve([x+y+z-3, 2*x+2*y+2*z-6], x,y,z)
print(solution)
 


