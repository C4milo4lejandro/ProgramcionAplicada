sombra2 =[[0.8125, 0.8125],[2.1666, 2.1666],
          [0.8125, 1.6250],[2.1666, 4.3330],
          [1.6250, 0.8125],[1.3333, 2.1666],
          [1.6250, 1.6250],[4.3333, 4.3333]]

error_objetivo = 1.3
w_encontrado = None
max_intentos = 1000

for intento in range(max_intentos):
    # Genera pesos aleatorios entre -2 y 2
    w = [[random.uniform(-2, 2) for _ in range(3)] for _ in range(2)]

    # Calcula la proyección del cubo con estos pesos
    y_calc = calcula_salidas(cubo, w)

    # Calcula el error respecto a sombra2
    error = calcula_error(sombra2, y_calc)

    if error < error_objetivo:
        w_encontrado = w
        print(f"Se encontró una matriz 'w' con error menor a {error_objetivo} en el intento {intento+1}!")
        print("w =", w_encontrado)
        print("Error calculado =", error)
        break

if w_encontrado is None:
    print(f"No se encontró un 'w' con error menor a {error_objetivo} después de {max_intentos} intentos.")

y_calc = calcula_salidas(cubo, w_encontrado)
dibuja_comparacion(sombra2, y_calc)
