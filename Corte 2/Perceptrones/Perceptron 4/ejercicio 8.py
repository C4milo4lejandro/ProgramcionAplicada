import numpy as np
import matplotlib.pyplot as plt

# Coordenadas 3D del cubo
cubo = [[0.5, 0.5, 0.5],
        [0.5, 0.5, 1.0],
        [0.5, 1.0, 0.5],
        [0.5, 1.0, 1.0],
        [1.0, 0.5, 0.5],
        [1.0, 0.5, 1.0],
        [1.0, 1.0, 0.5],
        [1.0, 1.0, 1.0]]

# Matriz de pesos entrenada
w = [[0.3, 1.0, 0.0],  # Proyección en eje x
     [0.8, 0.3, 0.5]]  # Proyección en eje y

# Función de proyección lineal: y = w·x
def calcula_salida(x, w):
    return [sum(wi * xi for wi, xi in zip(w_linea, x)) for w_linea in w]

# Aplicar la transformación lineal a todo el cubo
sombra_lineal = [calcula_salida(x, w) for x in cubo]

# Proyección no lineal basada en geometría y fuente de luz en (0, 0, d)
def proyecta_fuente_luz(x, d=2.0):
    x1, x2, x3 = x
    denom = d - x3
    y1 = (x1 * d) / denom
    y2 = (x2 * d) / denom
    return [y1, y2]

sombra_no_lineal = [proyecta_fuente_luz(x, d=2.0) for x in cubo]

# Función para calcular el error cuadrático medio entre dos sombras
def calcula_error(y_a, y_b):
    error = 0
    for ya, yb in zip(y_a, y_b):
        for i in range(len(ya)):
            error += (ya[i] - yb[i])**2
    return error / (len(y_a) * len(y_a[0]))

# Comparación de errores
error_lineal_vs_lineal = calcula_error(sombra_lineal, sombra_lineal)
error_lineal_vs_no_lineal = calcula_error(sombra_lineal, sombra_no_lineal)

print(f"Error sombra_lineal vs. sombra_lineal (perfecto): {error_lineal_vs_lineal:.5f}")
print(f"Error sombra_lineal vs. sombra_no_lineal       : {error_lineal_vs_no_lineal:.5f}")
