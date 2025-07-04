import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

companies = ['Company W', 'Company X', 'Company Y', 'Company Z']
#Crea un array con nombres de empresas
market_share = [40, 20, 20, 10]
#Crea un array con valores asignables
#en caso de que el total no sea 100, el gráfico aproximará los valores al total de 100

plt.pie(market_share, labels=companies, autopct='%1.1f%%', colors=['blue', 'orange', 'green', 'red'])
#Crea un gráfico de pastel
#labels asigna los nombres de las empresas
#autopct muestra el porcentaje en cada sección
plt.title("Market Share by Company")
#Añade título al gráfico
plt.show()
