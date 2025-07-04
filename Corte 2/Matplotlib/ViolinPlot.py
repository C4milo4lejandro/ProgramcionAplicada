import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data = np.random.randn(1000)
#Genera 1000 puntos aleatorios
plt.violinplot(data)
#Crea un gráfico en forma de violín
plt.title("Violin Plot")
#Añade título
plt.ylabel("Values")
#Añade etiqueta al eje y
plt.show()
