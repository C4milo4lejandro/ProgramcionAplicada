import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

regions = ['North', 'South', 'East', 'West']
#crea un array de 4 elementos
sales_data = np.random.randint(500, 5000, size=(4, 12))
#Crea un array de 4x12 elementos random entre 500 y 5000

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
#Crea una figura con 2 filas y 2 columnas de subgráficos
fig.suptitle('Monthly Sales by Region')
#Añade un título a la figura

for i, region in enumerate(regions):
    # Itera sobre las regiones y sus índices
    ax = axs[i // 2, i % 2]
    # Selecciona el subgráfico correspondiente
    ax.plot(sales_data[i], marker='o')
    # Dibuja una línea con marcadores para cada región
    ax.set_title(region)
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales (Units)")
# Añade etiquetas a los ejes

plt.tight_layout()
# Ajusta el diseño para que no se superpongan los subgráficos
plt.show()
