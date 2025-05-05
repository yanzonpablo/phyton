from clases.cuenta_bancaria import CuentaBancaria

#creamos instancia
cuenta = CuentaBancaria("pablo", 1000)

#obtener saldo inicial
print(cuenta.get_saldo())

# agregar 500
cuenta.depositar(500)
print(cuenta.get_saldo())

#retirar 300
cuenta.retirar(500)
print(cuenta.get_saldo())
