# #-----------------
# # FUNCIONES (Bloque de codigo reutilizable que realiza una tarea especifica)
# #-----------------

# Parametros son variables declaradas en la funcion que sirven como marcadores de posicion para los valores que 
# se pasan a la funcion cuando es llamada.
# def suma(a, b): # a y b son los parametros de la funcion
# res= a + b      # a y b 
# return res      # devuelve el resultado de la suma

#los argumentos son los # valores reales que se pasan a la funcion cuando es llamada.
# resultado = suma(3 + 5) # resultado es una variable local de la funcion
"""
def saludar(nombre, apellido="no hay"):
    print("Hola", nombre, apellido)

saludar("sergio")

''' # OJO
def saludar(*nombres):
    if len(nombres) > 1:
        print("Hola", nombres[0], nombre[1])
        else:
            print("Hola", nombres[0])
'''

def padre_orgulloso(nene1, nene3, nene2):
    print("Soy el padre de", nene1, nene2, nene3)
    print("Y el mas chico es:", nene3)

padre_orgulloso(nene1 = "Ricardito", nene2 = "Juan", nene3 = "Pedro") # uso de keyword arguments parea ordenar
"""
# ----------------------------------

from calendar import c


def devolver_mercaderia(mercaderia):
    for item in mercaderia:
        print(item)

lista_frutas = ["manzana", "banana", "pera"]

devolver_mercaderia(lista_frutas)

def suma(a, b):
    return a + b

print(suma(2, 5))

#------------------------------------
def devolver_mercaderia(mercaderia):
    """Documentar que hara la funcion"""
    pass # no hace nada pero no da error, y se puede usar para crear funciones vacias

#------------------------------------

def devolver_cuadrado(x):
    """devuelve el cuadrado del argumento pasado"""
    return x**2

print(devolver_cuadrado(x = 2)) 
#(*,x) 
#print(devolver_cuadrado(x = 2))#obliga a enviar keyword arguments

#(x, /) 
#print(devolver_cuadrado(2))#obliga a enviar posicion arguments

def calcular_resultado(a, b, /, *, c, d):
    print(a + b + c + d)

    calcular_resultado(1, 2, c=3, d=4) # / indica que los argumentos anteriores son obligatorios y deben ser enviados como posicion arguments

#-----------------------------------
def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return [suma, resta, multiplicacion, division] # devuelve una lista y se puede tupla con los resultados de las operaciones

print(operaciones(4, 2)) # llama a la funcion operaciones y le pasa los argumentos 2 y 5