class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular # usando __ hacemos privado el atributo
        self.__saldo = saldo_inicial

    # Setter (editor, configurador)
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print (f"deposito de {cantidad} fue exitoso")
        else:
            print("La cantidad a depositar debe ser mayor a cero")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"se ha retidado ${cantidad} exitosamente")
        else:
            print("fondos insuficientes o cantidad invalida")

    # Getter(obtener informacion privada a traves de un metodo publico)

    def get_saldo(self):
        return self.__saldo
    
    
    
