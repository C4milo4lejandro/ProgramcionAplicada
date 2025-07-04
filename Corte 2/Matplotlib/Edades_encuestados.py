import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

ages = np.random.randint(18, 65, size=2000)
#crea un array de 2000 elementos random entre 18 y 65

plt.hist(ages, bins=10, color='purple', edgecolor='black')
#Crea un histograma de edades
#bins define la cantidad de barras
plt.title("Age Distribution of Survey Participants")
#Añade título al gráfico
plt.xlabel("Age")
#Añade etiqueta al eje x
plt.ylabel("Number of Participants")
#Añade etiqueta al eje y
plt.show()
