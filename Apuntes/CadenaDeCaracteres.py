#3 comillas salto de linea
#txt = """
#Hola mundo
#"""
#-----------------------------

# trabajar con caracteres de cadenas de caracteres
#indice [0,1,2,3,4,5...]
# el espacio existe y se imprime
#txt = "Hola mundo"
#print(txt[4])

#-----------------------------
#len devuelve cuenta los caracteres de la cadena de caracteres y cuentan los saltos de linea y espacios
txt = """
Hola mundo
"""
print(len(txt))

#-----------------------------
# ver si existe palabra dentro de la cadena de caracteres
txt = "En este texto les expolcare acerca de la cadena de caracteres, en ingles llamadas string"
print("ingles" in txt) # devuelve True o False
print("JavaScript" not in txt) # devuelve True o False
#las busquedas son case sensitive, es decir, si escribo en mayuscula no lo encuentra

#slicing ponemos desde un indice hasta otro indice no incluido
txt = "En este texto les expolcare acerca de la cadena de caracteres, en ingles llamadas string"
print(txt[0:2])
print(txt[-7:]) # cuenta desde el final de la cadena de caracteres

#LOWERCASE (FUNCIONA)convierte a minuscula
print(txt.lower()) # devuelve la cadena de caracteres en minuscula

#UPPERCASE (FUNCIONA)convierte a mayuscula
print(txt.upper()) # devuelve la cadena de caracteres en mayuscula

# STRIP() (FUNCIONA)elimina los espacios en blanco al principio y al final de la cadena de caracteres
txt = "         DEJANDO ESPACIOS        "
txtCorregido= txt.strip()
print(txt.strip()) # devuelve la cadena de caracteres sin espacios al principio y al final

# Concatenar cadenas de caracteres (FUNCIONA) une dos cadenas de caracteres
a="Hola"
b="Mundo"
c= a + " " + b #concatenar cadenas de caracteres
print(c) # devuelve la cadena de caracteres concatenada

#-----------------------------------------------------------------

horas = 2
clases = 3
txt= "Hoy tengo " + str(0) + " horas de clase y " + str(1) + " clases"
print(txt.format(horas, clases)) # devuelve la cadena de caracteres concatenada con los valores de horas y clases

#escape de caracteres " \ " (FUNCIONA) para imprimir comillas dobles o simples dentro de la cadena de caracteres
txt = "Hola \"mundo\""
print(txt) # devuelve la cadena de caracteres con las comillas dobles dentro de la cadena de caracteres

txt = "La carpeta donde se encuentra el archivo es C:\\Users\\Usuario\\Documents\\archivo.txt"
#se coloca el doble \ para que no se interprete como una direccion
print(txt) # devuelve la cadena de caracteres con las comillas dobles dentro de la cadena de caracteres

#-----------------------------------------------------------------
# \n salto de linea (FUNCIONA) para imprimir un salto de linea dentro de la cadena de caracteres
txt = "Hola: \nmundo"
print(txt)
# \t tabulacion (FUNCIONA)
# \b backspace, borra 1 caracter a la izquierda

#metodos para cadena de caracteres

txt = "hola mundo, este es un texto de prueba"
print (txt.capitalize()) # devuelve la cadena de caracteres con la primera letra en mayuscula
print (txt.center(20)) # devuelve la cadena de caracteres centrada en 20 espacios
print (txt.count("a")) # devuelve la cantidad de veces que aparece la letra a en la cadena de caracteres
print (txt.endswith("prueba")) # devuelve True o False si la cadena de caracteres termina con la palabra prueba
print (txt.find("mundo")) # devuelve la posicion de la palabra mundo en la cadena de caracteres
print (txt.isdigit()) # devuelve True o False si la cadena de caracteres es un numero
print (txt.isdecimal()) # devuelve True o False si la cadena de caracteres es un numero decimal(no flotante)
print (txt.islower()) # devuelve True o False si la cadena de caracteres es minuscula