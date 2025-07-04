import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
#Crea 9 puntos entre 0 y 10
#El tecer número define la "suavidad" de la curva
y1 = np.sin(x)
#Asigna a y1 la gráfica del seno para los valores de x
y2 = np.cos(x)
#Asigna a y2 la gráfica del coseno para los valores de x

plt.plot(x, y1, color='red', label='sin(x)')
#Crea la gráfica con los puntos x y sus senos de color rojo
plt.plot(x, y2, color='green', label='cos(x)')
plt.title("No amigable con daltónicos")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

plt.plot(x, y1, color="#2954C9", label='sin(x)')
#Crea la gráfica con los puntos x y sus senos de color morado
plt.plot(x, y2, color='#D55E00', label='cos(x)')
plt.title("Amigable con daltónicos")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
