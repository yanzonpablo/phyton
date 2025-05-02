def division (dividendo, divisor):
    try:
        resultado = dividendo / divisor
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero")
        resultado = None
    return resultado

print(division(5, 0))

print("Pudo llegar hasta aca")


#------------------------------
def obtener_entero(texto):
    try:
        entero = int(texto)
    except ValueError:
        print("No se puede mapear a entero un texto")
        entero = None
    return entero
    
print(obtener_entero("abs"))
print(obtener_entero("123"))