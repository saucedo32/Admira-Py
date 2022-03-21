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


PERSONAS = 10
LIMITE_CUENTA = 100


cuenta = 0
persona = 0
giro = "horario"


for ciclo in range(LIMITE_CUENTA):
    cuenta = cuenta + 1 # se aumenta en 1 contador general

    if (giro == "horario"):
        if (persona == PERSONAS):
            persona = 0
        persona = persona + 1 # se suma 1 a contador de persona
    else:
        if (persona == 1):
            persona = PERSONAS + 1
        persona = persona - 1 # se resta 1 a contador de persona
    
    print(persona, cuenta)
    
    if (cuenta % 8 == 0): # cuenta es perfectamente divisible por 8
        if (giro == "horario"):
            giro = "antihorario"
        else:
            giro = "horario"
