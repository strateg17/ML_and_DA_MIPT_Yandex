import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.optimize

def f(x):
    y: float = math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)
    return y

def h(x):
    y2: int = int(f(x))
    return y2

# One dimension array for computation of X
x = np.array([int(i) for i in range(1,31)]).reshape(30,1)
print(x, '\n')

# SciPy optimize for x0 = 30 and function h(x)
print(scipy.optimize.minimize(h, [[30]], method='BFGS'), '\n')

# SciPy optimize for differential evolution for interval = [1, 30] and function h(x)
bounds = [(1, 30)]
print(scipy.optimize.differential_evolution(h, bounds), '\n')

# Chart analysis
x = np.linspace(0, 30, 1000)
y = np.array([h(x) for x in x])

# Creation of the figure
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, y, label='linear')  # Plot some data on the axes.
ax.set_xlabel('x')  # Add an x-label to the axes.
ax.set_ylabel('y = int(f(x))')  # Add a y-label to the axes.
ax.set_title("h(x) function chart")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
