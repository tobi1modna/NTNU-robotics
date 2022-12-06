import sympy

a0, a1, a2, a3, a4, a5 = sympy.symbols("a_0, a_1, a_2, a_3, a_4, a_5")
A = sympy.Matrix([[1, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 1, 1],
                 [0, 0, 0, 3, 4, 5],
                 [0, 0, 0, 6, 12, 20]])
b = sympy.Matrix([0, 0, 0, 1, 0, 0]).T
x = sympy.linsolve((A, b), a0, a1, a2, a3, a4, a5)
print(x)


