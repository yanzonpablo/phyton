## FUNCIONES DE ORDEN SUPERIOR ( SON AQUELLAS QUE REBIEN Y DEVUELVEN FUNCIONES COMO ARGUMENTO)

#-------------------------------------
# # MAP:(TOMA UN A FUNCION Y UN ITERABLE COMO ARGUMENTO Y APLICA LA 
# FUNCION A CADA ELEMENTO DEL ITERABLE)
#-------------------------------------

def cuadrado(x):
    return x * x
#Lista
numeros = [1, 2, 3, 4, 5]

cuadrados = list(map(cuadrado, numeros))

print(cuadrados)
#-------------------------------------
# FILTER:
#-------------------------------------
# FILTER (TOMA UN A FUNCION QUE DEVUELVE TRUE O FALSE Y UN ITERABLE Y DEVUELVE SOLO LOS ELEMENTOS 
# QUE DEVUELVAN TRUE COMO ARGUNMENTO DE LA FUNCION)

numeros_pares = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10 , 11, 12]

def es_par (num):
    return num % 2 == 0

pares = list(filter(es_par, numeros_pares))

print(pares)

# REDUCE: (TOMA UNA FUNCIO QUE RECIBA DOS ARGUMNTO Y UN ITERABLE 
# Y APLICA LA FUNCION ACUMULATIVA A LOS ELEMNTOS DEL ITERABLE)

#numeritos = [1, 2, 3, 4, 5]

#def suma(a, b):
#    return a + b

#sumatoria = reduce(suma, numeritos)

#print(sumatoria)

#---------------------------------------------------------------------

x = [1, 2, 3, 4, 5]

#cuadrados = list(map(cuadrado, numeros))
cuadrados = list(map(lambda x: x * x, numeros))

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(cuadrados)

print(pares)

#------------------------------
# Closure Functions
#------------------------------

def exterior(x):
    def interior(y):
        return x + y
    return interior

# CREAMOS UNA CLAUSURA LLANDO A LA FUNCION EXTERIOR

clausura = exterior(10)

# Ahora cuando llamemos a la funcion clausura va a recordar el valor que le dimos

resultado = clausura(5)

print(resultado)

#---------------------------------------------------------
# Decoradores y envoltorios (funciones) 
#---------------------------------------------------------

def decorador(funcion):
    def envoltorio():
        print("esta funcionalidad se dispararia antes de la funcion que nos pasen por arguemnto")
        funcion()
        print("esta funcionalidad se dispararia despues de la funcion que nos pasen por arguemnto")
    return envoltorio

def saludar():
    print("Hola, estoy saludando")

saludo_decorado = decorador(saludar)

saludo_decorado()
