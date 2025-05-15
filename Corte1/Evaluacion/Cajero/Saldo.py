saldo = 0.0

def obtener_saldo():
    return saldo

def depositar(cantidad):
    global saldo
    saldo += cantidad

def retirar(cantidad):
    global saldo
    if cantidad <= saldo:
        saldo -= cantidad
        return True
    else:
        return False
