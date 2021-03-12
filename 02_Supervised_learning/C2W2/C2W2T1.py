import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('weights_heights.csv', index_col='Index')

data.plot(y='Height', kind='hist', color='red', title='Height (inch.) distribution')

data.head(5)

data.plot(y='Weight', kind='hist', color='green', title='Weight (lbs.) distribution')


def make_bmi(height_inch, weight_pound):
    meter_to_inch, kilo_to_pound = 39.37, 2.20462
    return (weight_pound/kilo_to_pound) / \
           (height_inch/meter_to_inch)**2


data['BMI'] = data.apply(lambda row: make_bmi(row['Height'],
                                              row['Weight']), axis=1)

sns.pairplot(data)


def weight_category(weight):
    if weight < 120:
        weight_cat = 1
    elif weight >= 150:
        weight_cat = 3
    else:
        weight_cat = 2
    return weight_cat


data['weight_cat'] = data['Weight'].apply(weight_category)

sns.boxplot(x='weight_cat', y='Height', data=data, whis=[0, 100], width=.6, palette='vlag')

data.plot(y='Height', x='Weight', kind='scatter', color='blue', title='Dependence of height from weight')


def function(w,x):
    return w[0]+w[1]*x


def error(w):
    return ((data['Height'] - (w[0] + w[1] * data['Weight']))**2).sum()


data.plot(x="Weight", y="Height", kind='scatter', color='blue', title='Dependence of weight from height')

start = data['Weight'].min()
end = data['Weight'].max()
tempX = np.linspace(start, end)
w1 = [60, 0.05]
w2 = [50, 0.16]
y1 = function(w1,tempX)
y2 = function(w2, tempX)
plt.plot(tempX, y1, color="red", label='$w0$, $w1$ =' + str(w1))
plt.plot(tempX, y2, color='orange', label='$w0$, $w1$ =' + str(w2))
plt.legend(loc='best')
plt.show()

temp_w1=np.linspace(-5, 5 ,100)
temp_error =[error([50, i]) for i in temp_w1]
plt.xlabel('$w1$')
plt.ylabel('error')
plt.plot(temp_w1, temp_error, color='green')
plt.show()

import scipy.optimize as op


def opt_error(x):
    return error([50,x])

w1_opt = op.minimize_scalar(opt_error, bounds=(-5,5), method='bounded')
print(w1_opt)


data.plot(x='Weight', y='Height', kind='scatter', color='blue', title='Dependence of weight from height')
start = data['Weight'].min()
end = data['Weight'].max()
tempX = np.linspace(start, end)
tempW = [50, w1_opt.x]
tempY = function(tempW, tempX)
plt.plot(tempX, tempY, color='red', label='$w0$, $w1$ =' + str(tempW))
plt.legend(loc='best')
plt.show()

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

surf = ax.plot_surface(X, Y, Z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()





