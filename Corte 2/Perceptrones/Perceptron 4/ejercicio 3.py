#Define los valores de cada posición de un vector x
(x1, x2, x3) = (0.7, 0.3, 0.5)

#Define los valores de cada posición de otros dos vectores w
(w11, w12, w13) = (0.3, 1.0, 0.0)
(w21, w22, w23) = (0.8, 0.3, 0.5)

#Define las salidas multiplicando las posiciones definidas
y1= w11*x1 + w12*x2 + w13*x3
y2= w21*x1 + w22*x2 + w23*x3

#Imprime las salidas
print("y1:", y1)
print("y2:", y2)
