import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.optimize

def f(x):
    y: float = math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)
    return y

# One dimension array for computation of X
x = np.array([int(i) for i in range(1,31)]).reshape(30,1)
print(x, '\n')

# SciPy optimize for x0 = 2, 30
print(scipy.optimize.minimize(f, [[2]], method='BFGS'), '\n')

print(scipy.optimize.minimize(f, [[30]], method='BFGS'), '\n')

# Chart analysis
x = np.linspace(0, 30, 100)
y = np.array([f(x) for x in x])
print(y)

# Creation of the figure
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, y, label='linear')  # Plot some data on the axes.
ax.set_xlabel('x')  # Add an x-label to the axes.
ax.set_ylabel('y = f(x)')  # Add a y-label to the axes.
ax.set_title("f(x) function chart")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
