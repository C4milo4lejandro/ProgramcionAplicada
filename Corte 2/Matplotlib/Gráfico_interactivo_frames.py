import matplotlib

print(matplotlib.__version__)

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
#Genera 100 puntos entre 0 y 10
y = np.cos(x)
#Calcula el coseno de cada punto en x

fig, ax = plt.subplots()
#Crea una figura y un eje para el gráfico
line, = ax.plot(x, y)
#Defina la curva que va a animar

def update(frame):
    line.set_ydata(np.cos(x + frame / 10))
    #Actualiza los datos de la curva con un desplazamiento en el eje y
    return line
    #Devuelve la línea actualizada para la animación

#Crea la animación actualizando la curva en cada frame
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=100)
plt.show()
