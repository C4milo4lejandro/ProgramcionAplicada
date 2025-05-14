def mostrar_menu():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")

def calcular(num1, num2, opcion):
    if opcion == '1':
        return num1 + num2
    elif opcion == '2':
        return num1 - num2
    elif opcion == '3':
        return num1 * num2
    elif opcion == '4':
        if num2 == 0:
            return "Error: No se puede dividir entre cero"
        return num1 / num2
    elif opcion == '5':
        return num1 ** num2
    else:
        return "Opción no válida"

# Programa principal
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    mostrar_menu()
    opcion = input("Ingrese el número de la operación que desea realizar: ")

    resultado = calcular(num1, num2, opcion)
    print("Resultado:", resultado)

except ValueError:
    print("Error: Debe ingresar valores numéricos válidos.")
