# calculadora.py

import operaciones 

def mostrar_menu():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")

# Programa principal
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    mostrar_menu()
    opcion = input("Ingrese el número de la operación que desea realizar: ")

    if opcion == '1':
        resultado = operaciones.sumar(num1, num2)
    elif opcion == '2':
        resultado = operaciones.restar(num1, num2)
    elif opcion == '3':
        resultado = operaciones.multiplicar(num1, num2)
    elif opcion == '4':
        resultado = operaciones.dividir(num1, num2)
    elif opcion == '5':
        resultado = operaciones.potencia(num1, num2)
    else:
        resultado = "Opción no válida"

    print("Resultado:", resultado)

except ValueError:
    print("Error: Debe ingresar valores numéricos válidos.")
