#-----------------
# Conjuntos (SETS) (Coleccion no ordenada y mutable de elementos unicos) no acepta duplicados
#-----------------
# NO TIENE INDICE
# El booleano True con el numero 1 
# El booleano False con el numero 0 

conjunto_frutas = {"Manzana", "Platano", "Pera"}
                
                #constructor
conjunto_frutas2 = set(("Manzana", "Platano", "Pera"))

longitud = len(conjunto_frutas)

print(longitud)

print(conjunto_frutas)

print(conjunto_frutas2)

#-----------------
# ACCEDER, AGREGAR Y ELIMINAR ITEMS EN SET
#-----------------

conjunto_frutas = {"Manzana", "Platano", "Pera"}
conjunto_frutas2 = {"Piña", "Mango", "Papaya"}
lista_frutas = ["Kiwi", "Uva"]

# Con update se puede agregar otro tipo de estructura
conjunto_frutas.update(lista_frutas)

# aGREGA ELEMENTOS DE conjunto_frutas2 AL 1
conjunto_frutas.update(conjunto_frutas2)

# PREGUNTAR SI ESTA UN ELEMENTO
print("banana" in conjunto_frutas)

for frutas in conjunto_frutas:
    print(frutas)

conjunto_frutas.add("Banana")
print(conjunto_frutas)

# BORRAR ELEMENTOS
conjunto_frutas = {"Manzana", "Platano", "Pera"}
# Es igual
conjunto_frutas.remove("Pera")
conjunto_frutas.discard("Pera")

# Borra un elemento aleatoriamente
conjunto_frutas.pop()

#borrar todo dejando vacio el conjunto
conjunto_frutas.clear()
print(conjunto_frutas)

#Borra todo completo
del conjunto_frutas

#-----------------
# Juntar conjuntos y bucles en conjuntos
#-----------------

conjunto_letras = {"a", "b", "c"}
conjunto_numeros = {"1", "2", "3"}

union = conjunto_letras.union(conjunto_numeros)
# Es igual al ej. anterior 
# union = conjunto_letras | conjunto_numeros

print(union)

#Ejemplo especial

set_tecnologia_universidad = {"Python", "Java", "C++"}
set_tecnologia_empresa = {"Python", "TypeScript", "GoogleCloud"}

#set3 = set_tecnologia_universidad.intersection(set_tecnologia_empresa)

# Es igual al ej. anterior
# set3 = set_tecnologia_universidad & set_tecnologia_empresa
#set_tecnologia_universidad.intersection_update(set_tecnologia_empresa)

# opuesto de intersection_update
#set3 = set_tecnologia_universidad.difference(set_tecnologia_empresa)
set3 = set_tecnologia_universidad.difference_update(set_tecnologia_empresa)

# Es igual al ej. anterior
set_tecnologia_universidad - set_tecnologia_empresa

print(set_tecnologia_universidad)


conjunto_frutas = {"Manzana", "Platano", "Pera"}
# No tiene indice, la unica forma de recorrer es con un bucle for

for frutas in conjunto_frutas:
    print(frutas)

#Metodo copiar
conjunto_frutas = {"Manzana", "Platano", "Pera"}
conjunto_copia = conjunto_frutas.copy()
print(conjunto_copia)