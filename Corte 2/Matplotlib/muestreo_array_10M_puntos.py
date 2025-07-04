import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

x_huge = np.linspace(0, 100, 10000)
#Genera un array de 10,000 puntos entre 0 y 100
y_huge = np.sin(x_huge) + np.random.normal(0, 0.1, size=x_huge.shape)
#Calcula el seno de cada punto en x y añade ruido aleatorio

# Downsample the data
x_downsampled = x_huge[::10]
#Toma cada décimo punto de x_huge
y_downsampled = y_huge[::10]
#Toma cada décimo punto de y_huge

plt.plot(x_downsampled, y_downsampled)
#Crea el gráfico con los datos reducidos
plt.title("Downsampled Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
