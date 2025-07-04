import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1,10)
#genera un array de 1 a 9 random
temperature = np.random.normal(loc=5, scale=1, size=len(days))
#loc es la media, scale es la desviación estándar, size es el número de puntos a generar

plt.plot(days, temperature, color='orange', marker='x', linestyle='-')
# Dibuja una línea con marcadores en las temperaturas diarias de agosto
plt.title("Daily Temperatures in August", fontsize=16)
# Añade un título al gráfico y le da un tamaño
plt.xlabel("Day", fontsize=12)
# Añade una etiqueta al eje x y le da un tamaño
plt.ylabel("Temperature (°C)", fontsize=12)
# Añade una etiqueta al eje y y le da un tamaño
plt.grid(True)
# Añade una cuadrícula al gráfico
plt.legend(['Temperature'], loc='upper right')
# Añade una leyenda al gráfico y su posición
plt.annotate('Coldest Day', xy=(5, 10), xytext=(7, 5),arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.show()
