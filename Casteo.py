# texto (str)
variable1= "texto"
variable2= "123456"
variable3= "Texto123"

# numericas (int, float, complex)
variable4= 123456
variable5= 123.456
variable6= 123.456j

print(type(variable1))  # str (cadena de caracteres)
print(type(variable3))  # str (cadena de caracteres)
print(type(variable4))  # int (numeros enteros)
print(type(variable5))  # float (numeros decimales)
print(type(variable6))  # complex (numeros complejos)

# casteo de str a int
variableCasteada= int(variable2)
print(type(variableCasteada))  # str (cadena de caracteres)

# casteo de 
tupla = ("manzana", "banana", "cereza")
x= list(tupla) # convierte la tupla en una lista)
print(type(x))

#como se castea? (cambiar el tipo de dato) tipoDeDato("elDatoOriginal")
# con Type podemos saber el tipo de dato que estamos manejando

lista=[1,2,3,4,5]
x=tuple(lista)

print(type(x))