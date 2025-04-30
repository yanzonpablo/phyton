#-----------------RECURSION ------------
# def suma_naturales(n):
#     if n ==1:
#         return 1
#     else:
#         return n + suma_naturales(n-1)
    
# print(suma_naturales(5))

#-----------------RECURSION ------------
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

#-----------------RECURSION ------------

def contador(n):
    print(n) # imrpime 1
    n += 1 # suma 1 quedando 2
    if n < 10: # compara si es menor a 10
        contador(n) # Manda 2 al contador

contador(1)

#-------------DOCUMENTACION DE FUNCIONES-----------------

def suma(a,b):
    """
    esta funcion suma deos numeros y devuelve el resultado

    Args:
        a (int): El primer numero en sumar
        b (int): El segundo numero en sumar

    Returns:
        int: La suma de los dos numeros.
    """
    return a+b

print(suma(2,3))

#help(suma) # Igual al anterior

print(suma.__doc__)