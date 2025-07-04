import random

#Asigna a las variables 'a' y 'b' valores aleatorios entre -10 y 10
a = random.randint(-10, 10)
b = random.randint(-10, 10)

#Define las posiciones de un vector x
x1 = a/10
x2 = b/10
x3 = (a+b)/10

#Define los mismos valores anteriores para las posiciones de w
(w11, w12, w13) = (0.3, 1.0, 0.0)
(w21, w22, w23) = (0.8, 0.3, 0.5)

#Define las salidas
y1 = w11*x1 + w12*x2 + w13*x3
y2 = w21*x1 + w22*x2 + w23*x3

#Imprime las salidas
print("y1:", y1)
print("y2:", y2)
