import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

x_huge = np.linspace(0, 100, 10000)
#Crea un array de 10000 elementos entre 0 y 100

y_huge = np.sin(x_huge) + np.random.normal(0, 0.1, size=x_huge.shape)
#saca el seno de cada valor en x
# y_huge añade un ruido aleatorio con una desviación estándar de 0.1

bins = np.linspace(0, 100, 100)
# Divide el rango de x_huge en 100 intervalos

y_aggregated = [np.mean(y_huge[(x_huge >= bins[i]) & (x_huge < bins[i+1])]) for i in range(len(bins)-1)]
#agrupa los datos por rangos de x y saca el promedio de y en cada uno

plt.plot(bins[:-1], y_aggregated)
# Crea el gráfico con los datos agregados
plt.title("Aggregated Plot")
plt.xlabel("X")
plt.ylabel("Average Y")
plt.show()
