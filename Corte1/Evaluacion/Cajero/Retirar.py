import Vista
import Saldo

def Retiro():
    Vista.vistaRetirar()
    try:
        cantidad = float(input(">> "))
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return
        if Saldo.retirar(cantidad):
            print(f"Retiro exitoso. Saldo restante: {Saldo.obtener_saldo()}")
        else:
            print("Fondos insuficientes.")
    except ValueError:
        print("Ingrese un número válido.")

