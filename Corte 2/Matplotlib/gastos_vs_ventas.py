import matplotlib

print(matplotlib.__version__)

import numpy as np
import matplotlib.pyplot as plt

ad_spend = np.random.randint(50, 1000, size=50)
#Genera un array de 50 elementos random entre 50 y 1000
sales = ad_spend * np.random.uniform(0.8, 1.2, size=50)
#Genera un array de 50 elementos random entre 0.8 y 1.2
#Multiplica ambos arrays

plt.scatter(ad_spend, sales, color='green')
#Crea un gráfico de dispersión
plt.title("Advertisement Spending vs. Sales")
# Añade un título al gráfico
plt.xlabel("Ad Spend (USD)")
# Añade una etiqueta al eje x
plt.ylabel("Sales (Units)")
# Añade una etiqueta al eje y
plt.show()
# Muestra el gráfico
