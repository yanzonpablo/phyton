"""
visa = True
pasaporte = False

if visa and pasaporte:
    print("Puede viajar a cualquier país")
elif pasaporte and not visa:
    print("Puede viajar a cualquier país que no requiera visa")
else:
    print("No puede viajar a ningún país")"""

edad = 41

if edad < 18 or edad >40:
    if edad < 18:
        print("No pueden ingresar a la disco menores de edad")
    else:
        print("No pueden ingresar a la disco mayores de 40 años")
elif edad >= 18 and edad <= 40:
    print("Puedes ingresar a la disco")
