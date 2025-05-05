from clases.heroe import Heroe
from clases.villano import Villano

superman = Heroe("Superman", 100, "volar")
joker = Villano("Joker", 80, "Robar bancos")

#--------------------------------
superman.identificarse() # Heredado
superman.mostrar_salud() # Heredado+
superman.mostrar_poder() # Metodo comportamiento propio de heroe

joker.identificarse()# Heredado
joker.mostrar_salud() # Heredado+
joker.mostrar_habilidad() # metodo comoportamiento proio de villano