texto = "hola mundo"
texto_con_espacios = "   texto con espacios   "
texto_separado = "Pythom,JavaScript,React,Java"
lista = ["Hola", "Juan", "Carlos"]
numeros = "1234567890"
espacio = "          "
repeticion = "manzana, naranja, manzana, pera, manzana"

print("capitalize:", texto.capitalize()) # Convierte la primera letra en mayúscula y el resto en minúscula
print("upper:", texto.upper()) # Convierte todos los caracteres a mayúscula
print("lower:", texto.lower()) # Convierte todos los caracteres a minúscula
print("strip:", texto_con_espacios.strip()) # Elimina los espacios en blanco al principio y al final de la cadena
print("replace:", texto_con_espacios.replace("espacios", "gracia")) # Reemplaza una subcadena por otra
print("split:", texto_separado.split(",")) # Separar txto es items de una lista
print("join:", ",".join(lista)) # Une los elementos de una lista en una cadena
print("find:", texto.find("mundo")) # Musestra la posicion donde arranca el texto ingresado
print("index:", texto.index("mundo")) # Musestra la posicion donde arranca el texto ingresado
print("rfind:", repeticion.rfind("manzana")) # Musestra la posicion donde arranca el texto ingresado (de derecha a izquierda)
print("startswith:", texto.startswith("hola")) # Verifica si la cadena comienza con el texto ingresado
print("endswith:", texto.endswith("mundo")) # Verifica si la cadena termina con el texto ingresado
print("isdigit:", numeros.isdigit()) # Verifica si todos los caracteres son numeros (espacios no son numeros)
print("isalpha:", texto.isalpha()) # Verifica si todos los caracteres son letras (espacios no son letras)
print("isalnum:", numeros.isalnum()) # Verifica si todos los caracteres son alfanumericos (espacios no son alfanumericos)
print("isspace:", espacio.isspace()) # Verifica si el string solo esta hecho espacios
print("count:", repeticion.count("manzana")) # Cuenta la cantidad de veces que aparece la palabra ingresada
