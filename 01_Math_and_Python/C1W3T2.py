import numpy as np
import math
import scipy.optimize

def f(x):
    y: float = math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)
    return y

# One dimension array for computation of X
x = np.array([int(i) for i in range(1,31)]).reshape(30,1)
print(x, '\n')

# SciPy optimize.differential_evolution for bounds = [(1, 30)]
bounds = [(1, 30)]
print(scipy.optimize.differential_evolution(f, bounds), '\n')
