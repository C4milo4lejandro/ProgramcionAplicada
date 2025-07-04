#Varios vectores de entrada
def calcula_salidas(xs, w):
  #Inicializa el vector salida vacío
  ys = []
  #Para cada vector
  for x in xs:
    #Llamamos al cálculo de salida de un vector
    y = calcula_salida(x,w)
    #Agrega cada resultado a ys
    ys.append(y)
  return ys

#Primer vector definido con variable, y otro definido
xs = [[x1, x2, x3], [0.3, 0.6, 0.8]]
#Asigna la función 'calcula_salidas' a 'y_calc'
y_calc = calcula_salidas(xs, w)
y_calc
