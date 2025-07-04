import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

groupings = ['Musical Instruments', 'Furniture', 'Clothing', 'Food']
#Crea un array con los nombres de las agrupaciones
revenue = [50000, 30000, 20000, 40000]
#Crea un array con valores

plt.bar(groupings, revenue, color='yellow')
#Crea un gráfico de barras
plt.title("Revenue by Product Grouping")
#Añade título al gráfico
plt.xlabel("Group")
#Añade etiqueta al eje x
plt.ylabel("Revenue (EURO)")
#Añade etiqueta al eje y
plt.show()
