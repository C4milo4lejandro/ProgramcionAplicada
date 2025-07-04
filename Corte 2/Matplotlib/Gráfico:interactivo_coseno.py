import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
#Genera 100 puntos entre 0 y 10
y = np.cos(x)
#Calcula el coseno de cada punto en x

fig, ax = plt.subplots()
#Crea una figura y un eje para el gráfico
ax.plot(x, y)
#Dibuja la curva del coseno

def on_click(event):
    #Determina qué hacer al hacer clic en el gráfico
    if event.xdata is not None and event.ydata is not None:
        #Verifica que las coordenadas del clic no sean None
        ax.plot(event.xdata, event.ydata, 'ro')
        # Marca el punto clickeado con un círculo rojo
        fig.canvas.draw()
        # Redibuja el gráfico para mostrar el nuevo punto
        # Imprime las coordenadas del clic en la consola
    print(f"Las coordenadas se 'clickearon' en: ({event.xdata}, {event.ydata})")

fig.canvas.mpl_connect('button_press_event', on_click)
# Conecta el evento de clic del ratón a la función on_click
plt.show()
# Muestra el gráfico interactivo
