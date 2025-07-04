import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)
#Genera 1000 puntos aleatorios de una distribución normal
plt.boxplot(data)
#Crea un boxplot de los datos
plt.title("Box Plot")
#Añade un título al gráfico
plt.ylabel("Values")
plt.show()

#La línea naranja representa la media
#La caja representa el 50% de los datos
#Los círculos muestran los datos más alejados del resto
