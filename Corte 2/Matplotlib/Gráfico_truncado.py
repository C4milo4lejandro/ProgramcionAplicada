import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.arange(10)
#Crea un array de 10 valores
y1 = np.random.randint(50, 100, size=10)
#Crea un array de 10 valores aleatorios entre 50 y 100
y2 = y1 + np.random.randint(-5, 5, size=10)
#Crea un array de 10 valores aleatorios entre -5 y 5 y los suma a y1

# Plot with truncated y-axis
plt.plot(x, y1, label='Data 1')
#Crea un gráfico de línea con x e y1
#label define la etiqueta de la línea
plt.plot(x, y2, label='Data 2')
plt.ylim(90, 100)
#Cambia el límite del eje y entre 90 y 100
plt.title("Gráfico con eje Y ajustado")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
#Se "hace zoom" en el límite del eje y

plt.plot(x, y1, label='Data 1')
#Crea un gráfico de línea con x e y1
#label define la etiqueta de la línea
plt.plot(x, y2, label='Data 2')
plt.title("Gráfico completo")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
