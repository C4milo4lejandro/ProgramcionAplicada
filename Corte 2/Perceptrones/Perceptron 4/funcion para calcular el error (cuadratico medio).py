def calcula_error(y_a, y_b):
  error = 0
  m = len(y_a)
  n = len(y_a[0])

#Rango definido en el número de vectores
  for j in range(m):
    yaj = y_a[j]
    ybj = y_b[j]
    #Rango definido en el número de elementos de cada vector
    for i in range(n):
      #Error cuadrático medio
      error = error+(yaj[i]-ybj[i])**2
    return error/(n*m)

error = calcula_error(sombra, y_calc)
print(f'El error de la salida es {error}')
