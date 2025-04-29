# #-----------------
# # Diccionarios en Python (colecciones no ordenada de pares clave-valor)
# #-----------------

# diccionario={
#     "nombre":"Juan", 
#     "edad":30,
#     "ciudad":"Madrid",
#     "telefono":123456789,
#     "tecnologias": ["Python", "Java", "C++"]}

# # print(diccionario)
# # # ACCEDER A UN ELEMENTO DEL DICCIONARIO POR SU CLAVE
# # print(diccionario["nombre"])

# # # ASIGNAR A UNA VARIABLE 
# # variable = diccionario.get("nombre")
# # print(variable)
# # # clave
# # claves = diccionario.keys() # devuelve una vista de las claves del diccionario
# # print(claves)

# claves = diccionario["primo"] = "Pedro"
# print(claves)

# # devuelve valores sin claves

# valores = diccionario.values() # devuelve una vista de los valores del diccionario
# print(valores)

# diccionario["primo"] = "Pepe" # agregar un nuevo elemento al diccionario
# valores = diccionario.values() # devuelve una vista de los valores del diccionario
# print(valores)

# items = diccionario.items() # devuelve una vista de los valores del diccionario
# # Devuelve una tupla de clave valor

# if "nombre" in diccionario:
#     print("La clave existe")

#-----------------
# Diccionarios en Python (Cambiar, afregar y eliminar pares clave-valor)
#-----------------

diccionario={
    "nombre":"Juan", 
    "edad":30,
    "tecnologias": ["Python", "Java", "C++"]}
# ACTUALIZAR Y AGREGAR ELEMENTOS AL DICCIONARIO
diccionario["nombre"] = "Pedro Juan" # Cambiar el valor de una clave existente
diccionario.update({"nombre": "Ricardo Ramirez", "edad": 25}) # Cambiar el valor de una clave existente
diccionario.update({"edades": 25}) # Cambiar el valor de una clave existente
diccionario["ciudad"] = "Valencia" # Agregar un nuevo elemento al diccionario cuando no exite clave

# BORRAR ELEMENTOS DEL DICCIONARIO
diccionario.pop("edad") # Eliminar un elemento del diccionario por su clave
diccionario.popitem() # Eliminar el ultimo elemento del diccionario
del diccionario["nombre"] # Eliminar un elemento del diccionario por su clave
diccionario.clear() # Eliminar todos los elementos del diccionario
print(diccionario)


#-----------------
# Diccionarios en Python (copiar diccionarios y utilizacion de bucles)
#-----------------

diccionario = {
    "nombre":"Juan", 
    "edad":30,
    "tecnologias": ["Python", "Java", "C++"]}

diccionario2 = diccionario.copy() # Copiar un diccionario

for key in diccionario:
    print("Clave",key, "Valor:", diccionario[key]) # Iterar sobre las claves del diccionario

for values in diccionario.values():
    print("Valore:", values) # Iterar sobre los valores del diccionario

for x,y in diccionario.items():
    print(x,y) # Iterar sobre los elementos del diccionario (clave, valor)

#-----------------
# Diccionarios anidados (diccionarios dentro de diccionarios)
#-----------------

familia = {
    "padre": {"nombre":"Raul", 
    "profesion": "Carpintero"
    },
    "madre": {"nombre":"Patricia",
    "profesion": "Abogada"
    },
    "hijo": {"nombre":"Pedro",
    "profesion": "desempleado"
    }
}

print(familia["padre"]["profesion"]) # Acceder a un elemento del diccionario anidado
#    P,M,H      N,P
for pariente, data in familia.items():
    print(pariente)
#                   N,P
    for clave in data:
        print(clave + ":", data[clave]) # Iterar sobre los elementos del diccionario anidado