# Coordenadas 3D de los vértices de un cubo
cubo = [[0.5, 0.5, 0.5],
        [0.5, 0.5, 1.0],
        [0.5, 1.0, 0.5],
        [0.5, 1.0, 1.0],
        [1.0, 0.5, 0.5],
        [1.0, 0.5, 1.0],
        [1.0, 1.0, 0.5],
        [1.0, 1.0, 1.0]]

# Coordenadas 2D de la sombra proyectada del cubo
sombra = [[0.5263, 0.5263],
          [0.5555, 0.5555],
          [0.5263, 1.0526],
          [0.5555, 1.1111],
          [1.0526, 0.5263],
          [1.1111, 0.5555],
          [1.0526, 1.0526],
          [1.1111, 1.1111]]

import numpy as np
import matplotlib.pyplot as plt

def dibuja(sombra):
  # Convertir la lista de coordenadas 2D a un array de NumPy
  p = np.array(sombra)

  # Dibujar los puntos proyectados (sombra de los vértices del cubo)
  plt.scatter(*p.T, color='black')  # .T transpone para que se pase como x, y

  # Lista de índices de los puntos que se conectan con líneas
  # para dibujar las aristas del cubo proyectadas en 2D
  p1 = [sombra[0], sombra[2],
        sombra[6], sombra[4],
        sombra[0], sombra[1],
        sombra[3], sombra[2], sombra[3],
        sombra[7], sombra[6], sombra[7],
        sombra[5], sombra[4], sombra[5],
        sombra[1]]

  # Convertir los puntos conectados en un array
  p1 = np.array(p1)

  # Transponer para usar en plt.plot (x, y)
  l1 = np.transpose(p1)

  # Dibujar las líneas (aristas de la sombra del cubo)
  plt.plot(*l1, color='black')

  # Establecer límites del gráfico
  plt.axis([0, 1.2, 0, 1.2])

  # Mostrar el gráfico
  return plt.show()

# Llamar la función para dibujar la sombra del cubo proyectado
dibuja(sombra)
