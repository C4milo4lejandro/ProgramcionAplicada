import Vista
import Depositar
import Retirar
import Saldo

while True:
    Vista.vistaPrincipal()
    opcion = input("Ingrese su acción: ")

    if opcion == "1":
        Depositar.Deposito()
    elif opcion == "2":
        Retirar.Retiro()
    elif opcion == "3":
        Vista.vistaConsultarSaldo()
    elif opcion == "4":
        Vista.vistaDespedida()
        break
    else:
        Vista.vistaOpcionNoValida()

    input("\nPresione ENTER para continuar...")
