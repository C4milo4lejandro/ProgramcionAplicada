def entrenamiento(xs, w, y_esp, va = 0.1, epocas = 1, dibujar = True):
  w1 = w
  for k in range(epocas):
    y_calc = calcula_salidas(cubo,w1)
    print('Epoca:', k, 'error:', calcula_error(y_calc, sombra))

    if dibujar == True:
      dibuja(y_calc)

    for i in range(len(xs)):
      x = xs[i]
      ye = y_esp[i]
      yc = calcula_salida(cubo[i], w1)
      w1 = backprop_lin(x, w1, ye, yc, va)
  return w1

w = [[w11, w12, w13], [w21, w22, w23]]
w_final = entrenamiento(cubo, w, sombra, 0.5, 15)

print('w_final=', w_final)
