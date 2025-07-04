#Importar random para simular un ensayo y error con los números aleatorios
import random

#Definimos un valor para la variable que define el vector x
a = 2

#Definición del vector x
x = [a-3, a+1, a-1]

#Define la función producto punto entre x y w
def productop(w, x):
  #Deben ser del mismo tamaño
  if len(w) != len(x):
    raise ValueError("Los vectores deben tener la misma longitud")
  #Devuelve la suma de la multiplicación de los elementos de ambos vectores
  return sum(wi * xi for wi, xi in zip(w, x))

#Inicializa la variable en none
found_t = None
#Define un máximo de intentos
max_attempts = 1000000

#Un recorrido hasta el máximo de intentos
for attempt in range(max_attempts):
    #Da cuatro números aleatorios entre -10 y 10, sin pasarse del tamaño del vector x
    t = [random.randint(-10, 10) for _ in range(len(x))]
    #Asigna la función del producto punto a la variable 'y'
    y = productop(t, x)
    #Evalúa que la variable 'y' esté a una distancia muy pequeña de 10
    if abs(y - 10) < 1e-9:
        #Cuando se cumpla, que 'y' esté  auna distancia muy pequeña de 10, asigna los valores random 't' a 'found_t'
        found_t = t
        #Sale del bucle, porque ya encontramos lo que queríamos
        break

#Cuando se encuentra imprime el vector 't'
if found_t is not None:
    print("Se encontró un vector 't' tal que el producto punto con 'x' es aproximadamente 10:")
    print("x:", x)
    print("t:", found_t)
    print("Producto punto (y):", productop(found_t, x))
#Si no, imprime que no se encontró en los intentos dados
else:
    print(f"No se encontró un vector 't' que resulte en un producto punto de 10 después de {max_attempts} intentos.")
    print("Puedes intentar aumentar el número de intentos o el rango de valores para los elementos de 't'.")
