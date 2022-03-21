"""
EJERCICIO RONDA DE PERSONAS

Tareas realizadas:
- Contar en ronda de 1 en 1.
- Controlar límite de personas en ronda.
- Detectar cuenta divisible por 8 y cambiar en ese momento sentido de giro ronda

Tareas pendientes:
- Detectar cuenta divisible por 11 y saltar 1 persona, siguiendo mismo sentido de giro
Ej, si está contando horario la persona 8, la siguiente en contar deberá ser la 10; si es antihorario, la 6

- Permitir ingresar ctd de personas en ronda y límite de cuenta por consola, en lugar de indicarlos de forma fija
Ej: int(input("Personas en la ronda: "))

- Si el límite de cuenta es menor a la cantidad de personas en la ronda, no efectuar la cuenta, solo mostrar
en su lugar un mensaje de error con print
"""


# Introducir por consola la cantidad de personas en la ronda
PERSONAS = int(input("Personas en la ronda: "))

# LIMITE_CUENTA = 100
LIMITE_CUENTA = int(input("Límite de cuenta: "))

# Inicializacion de variables:
cuenta = 0
persona = 0
giro = "horario" # define horario vs antihorario
saltar = 0 # saltar = para numeros no divisibles por 11 // se pondra en 1 para % 11 = 0

if ( LIMITE_CUENTA < PERSONAS): # si hay menos personas que la cuenta debe disparar un error
    print("ERROR: La cantidad de personas es menor a la cuenta que se quiere realizar")

else: # Se realiza el conteo con las condiciones mencionadas en el enunciado
    while (cuenta < LIMITE_CUENTA):

        if (saltar == 0):
            cuenta = cuenta + 1 # se aumenta en 1 contador general
        else:
            cuenta = cuenta

        if (giro == "horario"):
            # que sucede para giro = horario
            if (persona == PERSONAS):
                persona = 0
            persona = persona + 1 # se suma 1 a contador de persona
        else:
            # que sucede si giro = antihorario
            if (persona == 1):
                persona = PERSONAS + 1
            persona = persona - 1 # se resta 1 a contador de persona
        
        # Si saltar es igual a 0 imprimimos las variables
        if (saltar == 0):
            print(persona, cuenta, giro)
        
        # si la cuenta es divisible por 8 hay que cambiar el sentido de giro
        # como caso especial si saltar = 0 porque tambien es divisible por 11 no se debe volver a cambiar sentido de giro
        if (cuenta % 8 == 0 and saltar == 0): # cuenta es perfectamente divisible por 8 y no hay que saltar al jugador
            if (giro == "horario"):
                giro = "antihorario"
            else:
                giro = "horario"

        # si la cuenta es divisible por 11 se debe saltar una persona en la dirección de giro
        if (cuenta % 11 == 0): # cuenta es perfectamente divisible por 11
            if (saltar == 0):
                saltar = 1
            else:
                saltar = 0




















