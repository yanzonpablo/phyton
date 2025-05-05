class Mago:
    #METOD ESPECIAL CONTRUCTOR
    def __init__(self, nombre, hechizos=None):
        self.nombre = nombre
        self.hechizos = hechizos if hechizos else []

    #METODOS ESPECIAL: TO STRING (se identifica una cadena de caracteres la instancia)
    def __str__(self):
        return f"hola mi nombre es {self.nombre}, el mago"
    
    def __len__(self):
        return len(self.hechizos)
    
    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.hechizos == otro.hechizos

    def __add__(self, otro):
        if isinstance(otro, Mago):
            return Mago(f"{self.nombre}-{otro.nombre}")
        else:
            raise TypeError("solo puedes combinar dos magos")