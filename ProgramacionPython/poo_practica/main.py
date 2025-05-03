# crear instancias de la clase perro
from clases.perro import Perro

# --------------------------------------------------------------------    
# crar instancia de la clase perro
perro1 = Perro("Firulais", 3) #esta llamando por detras al constructor pasandole nombre y edad.
perro2 = Perro("luna", 5) #al atruuto edad de la instancia le asignamos "edad" que nos envian como argumento el construactor

# --------------------------------------------------------------------
# Usando Template string con las variables propias de la instancia de una clase (objeto)
print(f"{perro1.nombre} tiene {perro1.edad} años y dice {perro1.ladrar()}")
print(f"{perro2.nombre} tiene {perro2.edad} años y dice {perro2.ladrar()}")