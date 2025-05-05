# #1. LISTAS (Lista) [coleccion ordenada y mutable] se pueden repetir elementos

# #indice   0(-6)      1(-5)    2(-4)    3(-3)   4(-2)   5(-1)
# lista = ["manzana", "platano", "pera", "mandarina", "fresa", "piña"]

# print(lista[0])
# print(lista[-3:-1])
# print(lista[-3:])
# if "mandarina" in lista:
#     print("La mandarina esta en la lista")

# lista[1] = "banana"
# lista[2] = "frutilla"
# lista[3] = "anana"

# lista[4:] = ["frutilla", "anana"]
# lista[3:4] = ["frutilla", "anana"]
# print(lista)

# lista.insert(2, "kiwi") # Agrega un elemento en la posicion indicada
# print(lista)

# lista.append("aguacate") # Agrega un elemento al final de la lista
# print(lista)

# lista1 = ["manzana", "platano", "pera"]
# lista2 = ["mandarina", "fresa", "piña"]

# lista1.extend(lista2) # Agrega los elementos de la lista2 a la lista1
# print(lista1)

# lista1 = ["manzana", "platano", "pera"]
# tupla = ("mandarina", "fresa", "piña")

# lista1.extend(tupla) # Agrega los elementos de la tupla a la lista1
# print(lista1)

# lista = ['manzana', 'platano', 'pera', 'mandarina', 'fresa', 'piña']
# lista.remove("mandarina") # Elimina el primer elemento que coincide con el valor indicado
# print(lista)

# lista = ['manzana', 'platano', 'pera', 'mandarina', 'fresa', 'piña']
# lista.pop(2) # Elimina el elemento en la posicion indicada (en este caso, el tercer elemento)
# lista.pop() # Elimina el ultimo elemento de la lista
# del lista[2] # Elimina el elemento en la posicion indicada (en este caso, el tercer elemento)
# del lista # Elimina la lista completa
# # lista.clear() # Elimina todos los elementos de la lista (la lista queda vacia)

# #-----------------------
# # Bucles en Listas
# #-----------------------

# frutas = ['manzana', 'platano', 'pera', 'mandarina', 'fresa', 'piña']

# # SHORTHAMD (abreviacion) (bucle for) para recorrer una lista
# [print(fruta) for fruta in frutas] # Recorre la lista y muestra cada elemento sin indice

# # Bucle for
# for fruta in frutas:
#     print(fruta) # Recorre la lista y muestra cada elemento sin indice

# for i in range(len(frutas)):
#     print(frutas[i])
#     print(i) # Recorre la lista y muestra cada elemento y su indice

# #--------------------------
# # BUCLE WHILE (tiene disponible indice)
# #--------------------------
# i = 0
# while i < len(frutas):
#     print(frutas[i])
#     i += 1 # Incrementa el valor de i en 1 en cada iteracion

# #--------------------------
# # Comprensión de listas (abreviaciones)
# #--------------------------

# frutas = ['manzana', 'platano', 'pera', 'mandarina', 'fresa', 'piña']

# frutas_con_e = []

# # for fruta in frutas:
# #     if "e" in fruta:
# #         frutas_con_e.append(fruta) # Agrega el elemento a la lista si cumple la condicion

# # abreviacion   dato
# # nombre        asignar  bucle            condicion
# frutas_con_e = [fruta    for fruta in frutas if "e" in fruta] # Agrega el elemento a la lista si cumple la condicion

# print(frutas_con_e)

# frutas2 = ['manzana', 'platano', 'pera', 'mandarina', 'fresa', 'piña']

# frutas2 = [fruta for fruta in frutas if fruta != "mandarina"] # Agrega el elemento a la lista si cumple la condicion

# #copia exacta de la lista
# copia = [fruta for fruta in frutas] # Agrega el elemento a la lista si cumple la condicion

# range = [x for x in range(10) if x < 5] # Agrega el elemento a la lista si cumple la condicion
# print(range) # [0, 1, 2, 3, 4]

# # abreviacion   dato
# # nombre        asignar  bucle            condicion
# frutas_con_e = [fruta    for fruta in frutas if "e" in fruta] # Agrega el elemento a la lista si cumple la condicion

# mayusculas = [fruta.apper() for fruta in frutas] # convierte lista en mayusculas
# print(mayusculas) # ['MANZANA', 'PLATANO', 'PERA', 'MANDARINA', 'FRESA', 'PIÑA']

# # abreviacion   dato
# # nombre        asignar  bucle            condicion
# lista_pablo = ["pablo" for fruta in frutas]
# print(lista_pablo) # ['pablo', 'pablo', 'pablo', 'pablo', 'pablo', 'pablo']

# #reemplazo de elementos en listas
# frutas = ['manzana', 'platano', 'pera', 'mandarina', 'fresa', 'piña']

# reemplza_fruta = [fruta if fruta != "pera" else "aguacate" for fruta in frutas] # Agrega el elemento a la lista si cumple la condicion

# #--------------------------
# # Ordenamiento de Listas    
# #--------------------------

# #indice     0(-6)      1(-5)     2(-4)     3(-3)       4(-2)   5(-1)
# frutas = ['manzana', 'platano', 'Pera', 'MAndarina', 'fresa', 'piña']
# numeros = [5, 2, 3, 1, 4]

# frutas.sort() # Ordena la lista de forma ascendente (de menor a mayor)
# print(frutas) # ['MAndarina', 'Pera', 'fresa', 'manzana', 'piña', 'platano']
# frutas.sort(reverse=True) # Ordena la lista de forma descendente (de mayor a menor)

# print(numeros) # [1, 2, 3, 4, 5]
# numeros.sort(reverse=True) # Ordena la lista de forma descendente (de mayor a menor)
# print(numeros) # [5, 4, 3, 2, 1]

# # ORDENA LA LISTA DE FORMA SENSIBLE (de menor a mayor)
# frutas.sort(key=str.lower) # Ordena la lista de forma ascendente (de menor a mayor) sin importar mayusculas o minusculas
# print(frutas) # ['fresa', 'mandarina', 'manzana', 'pera', 'piña', 'platano']

# #DAR VUELTA A LA LISTA
# frutas.reverse() # Da vuelta la lista (invierta el orden de los elementos)

#--------------------------
# Copiar y juntar listas
#--------------------------

#indice     0(-6)      1(-5)     2(-4)     3(-3)       4(-2)   5(-1)
frutas = ['manzana', 'platano', 'Pera', 'MAndarina', 'fresa', 'piña']

copia_frutas = frutas.copy() # Copia la lista completa (copia superficial)
print(copia_frutas) # ['manzana', 'platano', 'Pera', 'MAndarina', 'fresa', 'piña']

copia2_frutas = list(frutas) # Copia la lista completa (copia superficial)

frutas1 = ['manzana', 'platano', 'Pera']
frutas2 = ['MAndarina', 'fresa', 'piña']

frutas = frutas1 + frutas2 # Junta las dos listas (concatenacion)
print(frutas) # ['manzana', 'platano', 'Pera', 'MAndarina', 'fresa', 'piña']

frutas1.extend(frutas2) # Junta las dos listas (concatenacion)
print(frutas1) # ['manzana', 'platano', 'Pera', 'MAndarina', 'fresa', 'piña']

fruta = ["manzana", "platano", "pera", "manzana", "fresa", "piña"]
print(fruta.count("manzana")) # Cuenta la cantidad de veces que aparece la palabra ingresada

