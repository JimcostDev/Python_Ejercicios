import scipy.integrate as spi
import numpy as np


def f(x):
    return (-x**2) - (2*x) + (8)

pi = np.pi
a = -4
b = -3

result, error = spi.quad(f, a, b)

print(round(result,2))
