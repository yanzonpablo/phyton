# Operadores aritmeticos
# +   (sumar)
# -   (restar)
# *   (Multiplicar)
# /   (Dividir)
# //  para dividir enteros (floor division)
# %   resto / modulo(modulus)
# **  exponenciacion

a=7
b=4
c=a // b
d=a % b

print(c)
print(d)

# Operadores asignacion
# = asignacion

"""
x=10
x+= x
x-= x
x*= x
x/= x 
"""

# Operadores comparacion
# 2 == nos va a servir para comparar igualdad
# ! es la negacion
# != nos sirve para comparar diferencias
# >, <, >=, <= 

# Operadores Logicos
# and (nos va a devolver true si y solo si ambas afirmaciones son verdaderas)
# or (nos va a devolver true si alguna de las 2 afirmaciones son verdaderas)
# not (nos devolvera el opuesto al valor que siga)

x = 1
booleano = not x == 0
booleano = not x != 0
print (booleano)

# Operadores de Identidad
# is
# is not (negacion de is)

a = 5
b = 5
booleano = a is b
# booleano = a == b es lo mismo

print(booleano)

# Operadores de pertenencia
# in
# not in (negacion o inversa)

texto= "en este texto pondremos algunas tecnologias: Python, Django, R"

print("Django" in texto)

# Eliminar sensitive
texto= "en este texto pondremos algunas tecnologias: Python, Django, R"

textoMinusculas = texto.lower()
aBuscar = "python     ".strip().lower()

print(aBuscar in textoMinusculas)
