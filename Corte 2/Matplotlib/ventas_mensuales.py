import matplotlib

print(matplotlib.__version__)

import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1,13)
#crea un array de 1 a 12
sales = np.random.randint(2000, 4000, size=len(months))
# genera un array de números enteros aleatorios entre 2000 y 4000, con el mismo tamaño que months
plt.plot(months, sales, color='blue', linestyle='--', marker='o')
#con linestyle se da forma a la línea
#con color se da color a la línea
plt.title("Monthly Sales of Product ")
plt.xlabel("Month")
plt.ylabel("Sales (Units)")
plt.grid(True)
plt.show()
# Muestra el gráfico
