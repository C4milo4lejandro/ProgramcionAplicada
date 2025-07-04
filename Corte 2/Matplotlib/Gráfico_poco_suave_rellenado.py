import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.arange(0, 10, 1)
#Crea un arreglo de 0 a 10 con paso de 1
y1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#Crea un arreglo de 1 a 10
y2 = np.array([1, 3, 2, 5, 4, 6, 5, 7, 6, 8])
#Crea un arreglo en desordenado

plt.fill_between(x, y1, color='skyblue', alpha=0.5)
#fill_between rellena el area entre dos curvas
plt.fill_between(x, y2, color='orange', alpha=0.5)
plt.title("Gráfico de áreas apiladas engañoso")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Improved area chart with non-overlapping areas
plt.fill_between(x, y1, color='skyblue', alpha=0.5)
plt.fill_between(x, y1 + y2, y1, color='orange', alpha=0.5)
#fill_between ahora rellena el área entre y1 y la suma de y1 + y2
plt.title("Improved Stacked Area Chart")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
