# Palabras clave dentro de las estructuras de control

# Break:

contador = 0
while contador < 10:
    print(contador)
    if contador == 5:
        break # sale del bucle
    contador += 1 #incremento de 1 en 1

# Continue
for i in range(5): #imprime numeros impares
    if i % 2 == 0: # ver numeros impares
        continue
    print(i)

# Pass
edad = 19

if edad >18:
    print("puede ingresara esta institucion")
elif edad == 18:
    pass
else:
    print("no puede ingresar a esta institucion")