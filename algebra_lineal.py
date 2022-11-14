import numpy as np
import fractions
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

# Matriz A
A = np.array([[1, -1, -1, 0, 0], [0, 0, 1, -1, -1], [-2, -5, 0, 0, 0], [0, 5, -4, -5, -3], [0, 0, 0, 5, -2]])

# Vector b, terminos independientes
b = np.array([0, 0, -9, 0, 5])

# calculamos el determinante:
determinante = np.linalg.det(A)
print(f'El determinante es: {determinante}')
print()

try:
    # matriz no singular
    if determinante != 0:
        print('Solución del sistema:')
        x = np.linalg.solve(A, b)
        print(x)
        print()

        print('Comprobamos que A * x = b')
        print(np.matmul(A, x))
    else:
        print('La matriz es singular')
except Exception as e:
    print(f'Ha ocurrido una excepción: {e}')
