from typing import List, Any

import numpy as np
import math
import matplotlib.pyplot as plt

# Function
def f(x):
    y: float = math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)
    return y

# Equation solving for x = 1, 15
x1 = [1,15]
print(x1, '\n')
y1 = []
for item in x1:
    y1.append(f(item))

print(y1, '\n')

M1 = np.array([[1., float(x1[0])], [1., float(x1[1])]])
print(M1, '\n')

v1 = np.array([float(f(x1[0])), float(f(x1[1]))])
print(v1, '\n')

W1 = np.linalg.solve(M1, v1)
print(W1, '\n')

# Equation solving for x = 1, 8, 15
x2 = [1., 8., 15.]
print(x2, '\n')
y2 = []
for item in x2:
    y2.append(f(item))

print(y2, '\n')

M2 = np.array([[1., x2[0], x2[0]*x2[0]],
               [1., x2[1], x2[1]*x2[1]],
               [1., x2[2], x2[2]*x2[2]]])
print(M2, '\n')

v2 = np.array([float(f(x2[0])), float(f(x2[1])), float(f(x2[2]))])
print(v2, '\n')

W2 = np.linalg.solve(M2, v2)
print(W2, '\n')

# Equation solving for x = 1, 8, 15
x2 = [1., 8., 15.]
print(x2, '\n')
y2 = []
for item in x2:
    y2.append(f(item))

print(y2, '\n')

M2 = np.array([[1., x2[0], x2[0]*x2[0]],
               [1., x2[1], x2[1]*x2[1]],
               [1., x2[2], x2[2]*x2[2]]])
print(M2, '\n')

v2 = np.array([float(f(x2[0])), float(f(x2[1])), float(f(x2[2]))])
print(v2, '\n')

W2 = np.linalg.solve(M2, v2)
print(W2, '\n')


# Equation solving for x = 1, 4, 10, 15
x3 = [1., 4., 10.,  15.]
print(x3, '\n')
y3 = []
for item in x3:
    y3.append(f(item))

print(y3, '\n')

M3 = np.array([[1., x3[0], x3[0]*x3[0], x3[0]*x3[0]*x3[0]],
               [1., x3[1], x3[1]*x3[1], x3[1]*x3[1]*x3[1]],
               [1., x3[2], x3[2]*x3[2], x3[2]*x3[2]*x3[2]],
               [1., x3[3], x3[3]*x3[3], x3[3]*x3[3]*x3[3]]])
print(M3, '\n')

v3 = np.array([float(f(x3[0])), float(f(x3[1])), float(f(x3[2])), float(f(x3[3]))])
print(v3, '\n')

W3 = np.linalg.solve(M3, v3)
print(W3, '\n')

w_0 = str(round(W3[0], 2))
w_1 = str(round(W3[1], 2))
w_2 = str(round(W3[2], 2))
w_3 = str(round(W3[3], 2))

answer = ' '.join([w_0, w_1, w_2, w_3])
print('answer = ', answer)

submission = open('submission-2.txt', 'w')
submission.write(answer)
submission.close()
