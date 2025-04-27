# Estructura de control manejo de errores

# manejo de la division por cero

a = 10
b = 5
try: # intenta ejecutar el bloque
    resultado = a / b
    print(resultado)
except ZeroDivisionError: # se ejecuta si hay un error
    print("Error de division por cero")
finally: # sempre se ejecuta
    print("Fin del programa")
    resultado = 0

    print(resultado)