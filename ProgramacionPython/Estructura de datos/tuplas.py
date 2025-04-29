#----------------------------------------
#TUPLAS (coleccion de elementos inmutables y ordenados)
#----------------------------------------

frutas = ("Manzana", "Platano", "Cereza")
numeros = (1,2,3)
booleano = (True, False, True)
mixto = ("Manzana", "true", 1)

print(len(frutas))

#----------------------------------------
# ITEMS de las TUPLAS
#----------------------------------------
frutas = ("Manzana", "Platano", "Cereza", "Mandarina")

print(frutas[1])

if "Mandarina" in frutas:
    print("la fruta mandarina esta en lista")

#----------------------------------------
# ACTUALIZACION de las TUPLA
#----------------------------------------
#            0           1          2          3          4       5      6
frutas = ("Manzana", "Platano", "Cereza", "Mandarina", "Fresa", "Uva", "kiwi")

frutas2 = list(frutas) # lista

frutas2[1] = "Coco" # modifico la lista

frutas = tuple(frutas2) # convierto a tupla la lista y la reasigno a la variable original

print(frutas)

#------------------------------
# AGREGAR ELEMTOS A UNA TUPLA
#------------------------------

tuplas_frutas = ("Manzana", "Platano", "Cereza", "Mandarina", "Fresa", "Uva", "kiwi")

lista_frutas = list(tuplas_frutas) # lista

lista_frutas.append("Coco") # modifico la lista

tuplas_frutas = tuple(tuplas_frutas) # convierto a tupla la lista y la reasigno a la variable original

print(tuplas_frutas)

#------------------------------
# AGREGAR (concatenar) TUPLA A OTRA TUPLA
#------------------------------

tuplas_frutas = ("Manzana", "Platano", "Cereza", "Mandarina", "Fresa", "Uva", "kiwi")
tupla_verdura = ("Zanahoria", "Ajo", "Brocoli")

tuplas_frutas += tupla_verdura

print(tuplas_frutas)

#----------------OTRO EJEMPOLO----------

tuplas_frutas = ("Manzana", "Platano", "Cereza", "Mandarina", "Fresa", "Uva", "kiwi")
tupla_verdura = ("Zanahoria",)
tuplas_frutas += tupla_verdura
print(tuplas_frutas)

#------------------------------
# REMOVER ELEMENTO DE TUPLA
#------------------------------

tuplas_frutas = ("Manzana", "Platano", "Cereza", "Mandarina", "Fresa", "Uva", "kiwi")

tuplas_frutas = list(tuplas_frutas)
tuplas_frutas.remove("Manzana")
tuplas_frutas = tuple(tuplas_frutas)
print(tuplas_frutas)

#-----------------
# Elimina tupla
#-----------------

del tuplas_frutas

#-----------------
# desempaquetado de tuplas
#-----------------

tuplas_frutas = ("Manzana", "Platano", "Cereza", "Mandarina", "Fresa", "Uva", "kiwi")

(a, b, c, *d) = tuplas_frutas # desempaquetado de tupla en distintas variables
# El * pone todos los elementos que no tienen lugar asignado a esa letra

print(a)
print(b)
print(c)
print(d) #["Mandarina", "Fresa", "Uva", "kiwi"]

#-----------------
# BUCLES en tuplas
#-----------------
# Es igual a las listas

tuplas_frutas = ("Manzana1", "Platano1", "Cereza1", "Mandarina", "Fresa", "Uva", "kiwi")

for fruta in tuplas_frutas:
    print(fruta)

for i in range(len(tuplas_frutas)):
    print(tuplas_frutas[i], "con el indice", i)

i=0

while i < len(tuplas_frutas):
    print(tuplas_frutas[i])
    i+=1



tuplas_frutas = ("Manzana1", "Platano1", "Cereza1")
tuplas_frutas2 = ( "Mandarina", "Fresa", "Uva", "kiwi")

tuplas_fruta = tuplas_frutas + tuplas_frutas2

print(tuplas_fruta)

tuplas_fruta = tuplas_frutas *2 + tuplas_frutas2

print(tuplas_frutas.count("Manzana1"))

tuplas_frutas = ("Manzana1", "Platano1", "Cereza1", "Mandarina", "Fresa", "Uva", "kiwi")
print(tuplas_frutas.index("Uva"))