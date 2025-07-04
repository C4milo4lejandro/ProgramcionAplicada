"""Retropropagación:
    La derivada de una función permite determinar cómo aumenta
    la función en un punto determinado. Al seguir paso a paso la
    dirección en que disminuye la función, nos acercamos a un
    mínimo local.

    Derivando el error respecto al peso, podemos calcular un peso
    que disminuye el error

    Empieza en las capas de salida de perceptrones.
"""

#Importa la librería 'copy' para duplicar objetos sin referencias compartidas
import copy

#'x' es el vector de entradas
#'w' son los pesos en una matriz
# 'ye' es el vector de salida esperado
# 'yc' es el vector de salida calculado
# 'va' es la velocidad de aprendizaje

# Función de retropropagación para ajustar los pesos de una red lineal simple
def backprop_lin(x, w_ant, y_esp, y_calc, va = 0.1):
    #Crea una copia independiente de los pesos actuales
    w_sig = copy.deepcopy(w_ant)

    #Recorre cada neurona de salida
    for i in range(len(w_sig)):
        #Recorre cada peso conectado a la entrada
        for j in range(len(w_sig[0])):
            # Ajusta el peso
            w_sig[i][j] = w_sig[i][j] + va * x[j] * (y_esp[i] - y_calc[i])

    return w_sig

#Toma el primer vector de entrada del conjunto 'cubo'
x = cubo[0]
#Toma el primer vector de salida esperada del conjunto 'sombra'
ye = sombra[0]
#Calcula la salida actual de la red para 'x' usando pesos 'w'
yc = calcula_salida(x, w)
#Actualiza los pesos con retropropagación
w_calc = backprop_lin(x, w, ye, yc, 1)
# Muestra los nuevos pesos y el error total al aplicar los nuevos pesos a todas las entradas
w_calc, calcula_error(calcula_salidas(cubo, w_calc), sombra)
