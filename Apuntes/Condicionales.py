# CONDICIONALES
# ESTRUCUTA DE CONTROL CONDICIONALES QUE PERMITE EJECUTAR DIFERENTES
# BLOQUES DE CODIGO DEPENDIENDO DE SI SE CUMLEN CIERTAS CONDICIONES
"""
if condicion_1:
    # codigo a ejecutar si la condicion_1 es verdadera
elif condicion_2:
    # codigo a ejecutar si la condicion_2 es verdadera
else:
    # codigo a ejecutar si ninguna condicion anterior es verdadera
"""

#TERNARIAS EXPRESA UNA ESTRUCTURA CONDICIONAL EN 1 SOLA LINEA
#SE UTILIZA PRINCIPALMENTE PARA ASIGNAR VALORES A UNA VARIABLE EN FUNCION A 1 CONDICION

x = 10
resultado = "positivo" if x > 0 else "negativo"
print(resultado)

# BUCLES
# SON ESTRUCTURAS DE CONTROL QUE PERMITE EJECUTAR REPETIDAMENTE UN BLOQUE DE COD. 
# MIENTRAS SE CUMPLA UNA CONDICION O ESTA SE VUELVA FALSA

while condicion:
    "condicion a ejecutar mientras esta sea verdadera"

# BUCLE FOR
for indice in range(cantidad):
    "codigo a ejecutar en cada iteracion"

# MANEJO DE EXCEPCIONES
# ESTRUCTURAS DE CONTROL QUE PERMITEN MANEJAR ERRORES Y EXCEPCIONES QUE PUEDAN OCURRIR
# DURANTE LA EJECUCION DE UN PROGRAMA

try:
    # codigo que puede generar una excepcion
except TipoDeExcepcion as nombre_variable:
    # codigo para manejar la excepcion
finally:
    # codigo que se ejecuta, OPCIONAL

# PALABRAS CLAVE PARA CONTROL DE FLUJO
# FORMAN PARTE DEL CONJUNTO DE HERRAMIENTAS
# PROPORCIONA PARA COMTROLAR FLUJO DE EJECUCION Y LA LOGICA DEL PROGRAMA

# BREAK
    """
    for i in range(5)
        if i == 3: 
            break NO SIGUE HASTA 5 CORTA EN 3
        print(i) SE ESPERA: 0,1,2
    """
# CONTINUE
    """
    for i in range(5)
        if i == 3: 
            continue SIGUE HASTA 5 
        print(i) SE ESPERA: 0,1,2,4
    """

    # PASS
    
x = 10
if x > 5
        PASS #(NO HACE NADA, SOLO SIRVE COMO MARCADOR DE POSICION)
    else:
        print("x es menor o igual a 5")
    