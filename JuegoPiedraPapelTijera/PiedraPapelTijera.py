#Desafio
#mas de 1 turno (bucle while)

nombre1 = input("Como se llamara el jugador 1?: ")
nombre2 = input("Como se llamara el jugador 2?: ")
partidas = int(input("cuantas partidas quieren jugar?"))
jugadas = 0

while jugadas < partidas:
    
    jugador1 = input("Jugador 1, ¿Que elijes? ¿Piedra, Papel o Tijera?: ").lower()
    print(jugador1)
    jugador2 = input("Jugador 2, ¿Que elijes? ¿Piedra, Papel o Tijera?: ").lower()
    print(jugador2)

    condicion1 = jugador1 == "piedra" and jugador2 =="tijera"
    condicion2 = jugador1 == "papel" and jugador2 =="piedra"
    condicion3 = jugador1 == "tijera" and jugador2 =="papel"

    if jugador1 == jugador2:
        print("Empate")
    elif condicion1 or condicion2 or condicion3:
        print("Ha ganado:", nombre1)
    else:
        print("Ha ganado:", nombre2)

    jugadas += 1
