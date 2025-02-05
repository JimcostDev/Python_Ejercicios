import numpy as np
A = np.array([[1,2,3,4], [0,2,-1,5], [0,0,3,7]])
print(A)
resultado = np.linalg.matrix_rank(A)
print(resultado)