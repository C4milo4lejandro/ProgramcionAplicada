import Saldo

def vistaPrincipal():
    print ("+++++++++++++++++++++++++++++++++++")
    print ("Bienvenido al cajero de camilosoft")
    print ("+++++++++++++++++++++++++++++++++++")    
    print ("Selecciona qué acción quieres realizar:")
    print ( "Opcion 1: Ingresar Dinero" "\n"
            "Opcion 2: Retirar dinero" "\n"
            "Opcion 3: Consultar Saldo" "\n"
            "Opcion 4: Salir\n")

def vistaDepositar():
    print ("Ingrese la cantidad que va a depositar")

def vistaRetirar():
    print ("Ingrese la cantidad que va a retirar")

def vistaConsultarSaldo():
    print(f"Su saldo actual es: {Saldo.obtener_saldo()}")

def vistaDespedida():
    print ("Gracias por usar los cajeros Camilosoft")

def vistaOpcionNoValida():
    print ("Ingrese una opción o valor válido")
