import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1,10)
#genera un array de 1 a 9 random
temperature = np.random.normal(loc=5, scale=1, size=len(days))
#loc es la media, scale es la desviación estándar, size es el número de puntos a generar

plt.plot(days, temperature)
#Hace un gráfico con "days" y "temperature"
plt.title("Daily Temperatures in August")
#Añade título al gráfico
plt.xlabel("Day")
#Añade nombre al eje x
plt.ylabel("Temperature (°C)")
#Añade nombre al eje y

plt.savefig("daily_temperatures_august.png", dpi=300, bbox_inches='tight')
# Guarda el gráfico como imagen PNG con resolución de 300 dpi y ajusta los bordes
plt.savefig("daily_temperatures_august.pdf", format='pdf', bbox_inches='tight')
# Guarda el gráfico como PDF ajustando los bordes
