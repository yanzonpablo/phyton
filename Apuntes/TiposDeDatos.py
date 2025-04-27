#---------
#TEXTO
#---------

# - str(cadena de caracteres)
texto="Hola Mundo"

#---------
#NUMERICA
#---------

# - int(numeros enteros)
numero=10

# - float(numeros decimales)
numero_decimal=10.5

# - complex(numeros complejos)
numero_complejo=10+5j

#---------
#SECUENCIA
#---------

# - list(lista)
# coleccion ordenada y mutable de elementos
lista=[1,2,3,4,5]

# - tuple(tupla)
# tupla es una coleccion ordenada e inmutable de elementos
tupla=(1,2,3,4,5)

# - range(rango)
# secuencia inmutable de numeros
rango=range(1,10)

#---------
#MAPPING TYPE (MAPEO)
#---------

# - dict(diccionario)
# coleccion no ordenada de pares clave-valor
diccionario={"nombre":"Juan", 
             "edad":30, 
             "ciudad":"Madrid"}

#---------
#SET TYPES (CONJUNTO)
#---------

# - set(conjunto)
# coleccion no ordenada de elementos unicos(no permite repetir)
conjunto={1,2,3,4,5}

# - frozenset(conjunto inmutable)
# coleccion no ordenada de elementos unicos(no permite repetir) pero inmutable
conjunto_inmutable=frozenset({1,2,3,4,5})

#---------
#BOOLEAN TYPE (BOOLEANO)
#---------

# - boolean(puede ser verdadero o falso)
# True o False
booleano=True
booleano_2=False

#---------
#BINARY TYPES (BINARIO)
#---------

# - bytes(representa secuencia inmutable  de bytes)
bytes_data=b"datos"

# - bytearray(representa secuencia mutable de bytes)
bytearray_data=bytearray(b"datos")

# - memoryview(permite acceder a la memoria de objetos bytes sin hacer una copia)
memoria=memoryview(b"datos")

#---------
#NONE/NULL (NULO)
#---------

# - NoneType (representa la ausencia de valor o la no definicion)
nulo=None