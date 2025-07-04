import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1,10)
#genera un array de 1 a 9 random
temperature = np.random.normal(loc=5, scale=1, size=len(days))
#loc es la media, scale es la desviación estándar, size es el número de puntos a generar

plt.plot(days, temperature, marker='v')
# con marker='v' se indica cómo es cada punto
plt.title('Daily Temperatures in August')
#Le da nombre al gráfico
plt.xlabel('Day')
#Le da nombre al eje x
plt.ylabel('Temperature (°C)')
#Le da nombre al eje y
plt.grid(False)
#agrega o elimina la cuadrilla
