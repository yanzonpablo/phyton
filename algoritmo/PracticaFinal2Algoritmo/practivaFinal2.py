# Paso 1: Solicitar al usuario las medidas de la pieza del mueble en cms.
medidas_en_cms = float(input("Por favor, ingresar las medidas de la pieza del mueble(en cms): "))

# Paso 2: Convertir las medidas en centimetros a pulgadas.
medidas_en_pulgadas = medidas_en_cms / 2.54

#Paso 3: Mostrar el las medidas convertidas en pulgadas al usuario.
print("Las medidas en pulgadas de la pieza ingresada son:", medidas_en_pulgadas)