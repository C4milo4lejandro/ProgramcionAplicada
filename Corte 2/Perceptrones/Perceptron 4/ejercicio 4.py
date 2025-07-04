#Error objetivo
error_objetivo = 0.183
#Inicializa la matriz 'w' en none
w_encontrado = None
#Da un máximo de intentos
max_intentos = 1000000

#Itera para hallar un 'w' que se acomode
for intento in range(max_intentos):
  #Genera números aleatorios para llenar las posiciones de la matriz 'w' entre -2 y 2
  w = [[random.uniform(-2, 2) for _ in range(3)] for _ in range(2)]

  #Calcula los puntos proyectados con el 'w' aleatorio
  y_calc = calcula_salidas(cubo, w)

  #Calcula el error entre la proyección calculada y la sombra
  error = calcula_error(sombra, y_calc)

  # Verifica si el error es menor al error objetivo
  if error < error_objetivo:
    w_encontrado = w
    print(f"Se encontró una matriz 'w' con error menor a {error_objetivo} después de {intento + 1} intentos.")
    print("w:", w_encontrado)
    print("Error calculado:", error)
    break

#Si no se encuentra una matriz que cumpla la condición
if w_encontrado is None:
  print(f"No se pudo encontrar una matriz 'w' con error menor a {error_objetivo} después de {max_intentos} intentos.")
