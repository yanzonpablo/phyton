# Paso 1: Solicitar al usuario ingresar la edad del cliente.
edadCliente = int(input("Por favor, ingrese la edad del cliente: "))
permitido = True

# Paso 2: Verificar si la edad ingresada cumple con los requisito para ingresar a la discoteca.
if edadCliente >= 18:
    permitido = True
else:
    permitido = False
    
# ----------------------------------------------------------
# ejemplo simplificado de la estructura if-else (ternario)
# permitido =True if edadCliente >= 18 else False
# ----------------------------------------------------------

# Paso 3: Mostrarmos al usuario si su cliente puede o no ingresar a la discoteca.
if permitido:
    print("El cliente puede ingresar a la discoteca!")
else:
    print("El cliente NO puede ingresar a la discoteca por ser menor de edad")
