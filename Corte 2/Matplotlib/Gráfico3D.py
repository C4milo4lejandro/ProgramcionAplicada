import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = np.linspace(-5, 5, 100)
#Crea un array entre -5 y 5 con suavidad de 100
y = np.linspace(-5, 5, 100)
#Asigna las mismas características a Y
X, Y = np.meshgrid(x, y)
#Crea una matriz 2D de coordenadas X e Y
Z = np.sin(np.sqrt(X**2 + Y**2))
#Saca el cuadrado de X y Y, los suma, saca raíz y saca seno

fig = plt.figure()
#Crea una figura para el gráfico
ax = fig.add_subplot(111, projection='3d')
#1 fila, 1 columna, 1 posición
#Crea un gráfico 3D
ax.plot_surface(X, Y, Z, cmap='viridis')
#Crea una superficie con los valores de X, Y y Z
#Cmap es el mapa de colores
plt.title("3D Plot")
plt.show()

plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar(label='Z value')
#Crea un gráfico de contorno con los valores de X, Y y Z
plt.title("2D Contour Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
#Es otra manera de representar 3 valores dimensionales en 2D
