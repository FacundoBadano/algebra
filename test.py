import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches
import matplotlib as mpl
from mpl_toolkits.axes_grid1 import Divider, Size

import numpy as np

def get_triangle(P):
    m = P * 0.5
    n = P * 0.5 + np.array([0.5, 0])
    k = P * 0.5 + np.array([0.25, np.sqrt(3)/4])
    return np.array([m,n,k])

# triangulo unitario inicial
triangle = np.array([[0, 0],
              [1, 0],
              [0.5, np.sqrt(3)/2]])

# Crea un array que representa el triangulo Sierpinski hasta la etapa deseada
etapa = 2
for e in range(etapa):
    triangle = get_triangle(triangle)

# Se procede a graficar el triangulo
fig1 = plt.figure(facecolor='white')
ax1 = fig1.add_subplot(111, aspect='equal', facecolor='red')

for t in triangle.reshape(3**etapa,3,2):
    ax1.add_patch(mpatches.Polygon(t, fc="y"))

plt.show()