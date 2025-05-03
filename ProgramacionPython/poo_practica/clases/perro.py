class Perro:
    # metodo constructor (__init__)
    def __init__(self, nombre, edad):
        self.nombre = nombre # al atributo nombre de la instancia le asignamos "nombre" que nos encia como argumento en el constructos
        self.edad = edad # Al atrubto edad de la instancia le asignamos "edad" que no s envian como argumento en el constructor

    def ladrar(self):
        return "gauu"