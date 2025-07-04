def calcula_salida(x,w):
  #Inicializa la salida vacía
  y=[]
  #Para cada salida
  for i in range(len(w)):
    #Inicializa la sumatoria en 0
    yi=0
    #Para cada entrada
    for j in range(len(x)):
      #x tiene n elementos, y w tiene n*n elementos
      yi=yi+w[i][j]*x[j]
    #Almacena cada salida en el vector de salida
    y.append(yi)
  return y

x = [x1, x2, x3]
w = [[w11, w12, w13], [w21, w22, w23]]

calcula_salida(x,w)
