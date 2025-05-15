import Vista
import Saldo

def Deposito():
    Vista.vistaDepositar()
    try:
        deposito = float(input(">> "))
        if deposito <= 0:
            print("El valor debe ser positivo.")
            return
        Saldo.depositar(deposito)
        print(f"Tu depósito fue exitoso. Saldo actual: {Saldo.obtener_saldo()}")
    except ValueError:
        print("Por favor, ingrese un número válido.")
