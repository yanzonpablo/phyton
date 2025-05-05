import random

numero_secreto = random.randint(1,10) #numero aleatorio entre 1 y 100
cantidad_intentos = 0
cantidad_max_intentos = 5
adivinado = False

print("Bienvenido al juego de adivinanza")

while not adivinado and cantidad_intentos < cantidad_max_intentos: # mientras no haya adivinado el numero
    entrada = input("Ingrese un numero de 1 a 99: ") #TODO: convertir a numero
    numero = int(entrada) # convertir a numero

    if numero == numero_secreto:
        print("Felicidades, adivinaste el numero")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero es mayor")
    else:
        print("El numero es menor")
    cantidad_intentos +=1

if not cantidad_intentos < cantidad_max_intentos:
    print("superaste la cantidad de intentos, perdiste")