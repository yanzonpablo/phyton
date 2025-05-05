from clases.mago import Mago

merlin = Mago("Merlin", ["Bola de fuego", "rayo"])
gandalf = Mago("Gandalf", ["llamar a las aguilas coando termino la pelicula", "bola de fuego"])

print(merlin) #devuelve el metodo __str__ que habiamos generado
print(len(merlin)) #devuelve el metodo __len__ que habiamos generado

print(gandalf) #devuelve el metodo __str__ que habiamos generado
print(len(gandalf)) #devuelve el metodo __len__ que habiamos generado

print(merlin == gandalf) #false

copia_merlin = Mago("Merlin", ["Bola de fuego", "rayo"])
print(merlin == copia_merlin)# devuelve una comparacion usando criterios del metodo __eq__

mago_combinado = merlin + gandalf
print(mago_combinado)