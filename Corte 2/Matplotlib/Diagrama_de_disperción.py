import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(10000)
#Crea un array de 10000 valores
y = np.random.rand(10000)
#Crea un array de 10000 valores

plt.scatter(x, y)
#Crea un gráfico de disperción con x y y
plt.title("Scatter Plot with Over-plotting")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

plt.scatter(x, y, alpha=0.5)
#alpha reduce la opacidad de los puntos
plt.title("Scatter Plot with Reduced Over-plotting")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
