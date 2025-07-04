#Definimos 'a' y 'b'
a = 2
b = 2

#Definición de los vectores
x = [a-3, a+1, a-1]
w = [b+2, b-1, b]

#Función producto punto entre w y x
def productop(w, x):
  #Los vectores deben tener el mismo tamaño
  if len(w) != len(x):
    raise ValueError("Los vectores deben tener la misma longitud")
  #Multiplica cada posición de w por cada posición de x, aumentando igualmente las posiciones
  return sum(wi * xi for wi, xi in zip(w, x))

#Se asigna la función a la variable 'y'
y = productop(w, x)

#Imprime el resultado, que es el producto punto entre w y x
print("El valor de 'y' (producto punto) es:", y)
