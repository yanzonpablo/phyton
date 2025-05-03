from clases.personaje import Personaje

class Heroe(Personaje):
    def __init___(self, nombre, salud, poder):
        super().__init__(nombre, salud) # esto permite asignar valores a los atributos heredados
        self.poder = poder

    def mostrar_poder(self):
        print(f"{self.nombre} tiene el poder de {self.poder}")