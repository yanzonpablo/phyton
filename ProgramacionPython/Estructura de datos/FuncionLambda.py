#----------------------------------
# FUNCIONES LAMBDA
#----------------------------------

def duplicar(num):
    return num * 2

# print(duplicar(5))

#---------------Ej 1-------------------
# duplicar_lambda = lambda num: num * 2

# print(duplicar_lambda(5))
#--------------------------------------

#---------------Ej 2-------------------
multiplicar_lambda = lambda a, b: a * b

print(multiplicar_lambda(2, 6))

#---------------Ej 3-------------------
cuadrado_lambda = lambda num: num * num

print(cuadrado_lambda(4))

#---------------------------------------
def operaciones (operacion):
    if operacion == "suma": 
        return lambda x, y: x + y
    elif operacion == "resta": 
        return lambda x, y: x - y
    elif operacion == "multiplicar": 
        return lambda x, y: x * y
    else:
        return lambda x, y : x / y

suma = operaciones("suma")

print (suma(2, 5))

#---------------------------------------
def multiplicador (n):
    return lambda x: x * n

triplicar = multiplicador(3)

print(triplicar(5))

#---------------------------------------
#diccionadrio
estudiantes = [
    {"nombre": "juan", "edad": 30},
    {"nombre": "maria", "edad": 20},
    {"nombre": "jose", "edad": 10},
]

estudiantes_ordenados = sorted(estudiantes, key = lambda x : x["edad"])

print (estudiantes_ordenados)

#----------------------------------
# Funciones Como Argumento (callbacks)
#----------------------------------

def aplicar_funcion(func, valor):
    return func(valor)

def cuadrado(x):
    return x * x

def cubo(x):
    return x * x * x

print(aplicar_funcion(cuadrado, 3))
print(aplicar_funcion(cubo, 3))