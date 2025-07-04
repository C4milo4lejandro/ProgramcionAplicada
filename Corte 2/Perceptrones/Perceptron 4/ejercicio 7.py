# Error con respecto a la sombra original
error_sombra = calcula_error(sombra, y_calc)

# Error con respecto a la nueva sombra deseada
error_sombra2 = calcula_error(sombra2, y_calc)

# Imprimir resultados
print(f"Error con sombra original     : {error_sombra}")
print(f"Error con nueva sombra (sombra2): {error_sombra2}")

if error_sombra > error_sombra2:
    print("La nueva sombra es más precisa.")
else:
    print("La sombra original es más precisa.")
