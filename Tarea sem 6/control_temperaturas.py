

"""
CONTROL TEMPERATURA HORNO:

La tarea consiste en diseñar un algoritmo para controlar la temperatura de un horno de forma básica, leyendo valores desde un sensor y activando o desactivando 2 quemadores para aumentar o disminuir según se necesite.

Como no se dispone físicamente de los elementos, las lecturas se deben simular completando una matriz (lista) con valores al azar, usando el método randint de la librería random. Cuando sea necesario encender o apagar los quemadores, bastará con mostrar un print() con el mensaje en cuestión.

Etapas:

Ingresar una temperatura de prueba desde consola, mediante input, se usará para testear el algoritmo. No olvidar la conversión a entero (int). Si se ingresa 0, finaliza la ejecución de código.
Usando el comando random.randint(min, max), generar una lista de 50 lecturas, min será 300 y max 320 grados.
Obtener la lectura promedio de la lista.
Comparar esta lectura promedio con la temperatura del punto 1. Si la diferencia es mayor a 100 grados por debajo, se deben encender 2 quemadores; si es menor a 100, solo 1, y si está por arriba del valor promedio, apagar siempre los 2. En caso de estar dentro del rango correcto (300 a 320 grados), mostrar mensaje de horno a temperatura correcta.
Retornar a ingresar una nueva temperatura objetivo.
En el ejercicio se podrán integrar distintos puntos vistos (uso de variables / constantes, condiciones, ciclos y matrices).
"""

# Importo las librerías a usar
import random

# Hago un primer seteo de temp_ref != de 0 para que comience el programa
temp_ref = 1

while (temp_ref != 0):

    # Si la temperatura ingresada por consola es == 0 finaliza el programa.
    if(temp_ref == 0):
        break

    # Ingresar el valor de referencia por consola
    temp_ref = int(input("Introduzca una temperatura objetivo (en caso de introducir 0 finalizará el programa): "))


    # Si se introduce un valor igual a cero se imprime que finaliza el programa (en realidad finaliza después de finalizar el ciclo pero tengo que imprimirlo aquí)
    # Si se introduce un valor diferente de cero se imprime el valor y se realiza el procesamiento.
    if(temp_ref != 0):
        print("La temp. de referencia seleccionada es: ", temp_ref)
    else:
        print("Se finaliza el programa")

    # Genero 50 valores aleatorios:
    # Seteo una lista para completar valores random y suma_valores para poder calcular el promedio posteriormente
    # Por cuestiones de tiempo lo calculo por mas que el valor introducido sea 0 (en esos casos lo calculo pero no imprimo el resultado)
    v_random = [ ]
    suma_valores = 0
    valores_a_generar = 50

    for i in range (valores_a_generar):  
        v_random.append(random.randint(300, 320))
        suma_valores = suma_valores + v_random[i]
    #print("las mediciones fueron: ", v_random)

    # Calculo el promedio (lo imprimo solamente si el valor ingresado de referencia es distinto de 0)
    # Se calcula por más que el valor introducido sea 0 (en caso de que se introduzca un cero por consola se calcula pero no se imprime)
    prom_val_generados = suma_valores / valores_a_generar
    if(temp_ref != 0):
        print("El promedio de las mediciones es: ", prom_val_generados)

    # Resto promedio con valor ingresado inicialmente
    dif_valores = prom_val_generados - temp_ref


    # Decisiones a tomar en función de la temperatura promedio del horno y la ingresada por consola:
    # Agrego en todas las condiciones que la temperatura ingresada por consola sea diferente de cero.
    if (dif_valores <= -100 and temp_ref != 0):
        print("Se encienden 2 quemadores por difencia de temperatura menor -100 grados")
    if ((dif_valores < 0 and dif_valores > -100) and temp_ref != 0):
        print("Se enciende 1 quemador por difencia de temperatura entre 0 y -100 grados")
    if (dif_valores > 0 and temp_ref != 0):
        print("Se apagan 2 quemadores por estar arriba de la temperatura ingresada")

    # Si el horno se encuentra entre 300 y 320 grados imprimir que está en temperatura correcta.
    # Al crear valores random entre 300 y 320 nunca va a estar en otra temperatura que no sea la correcta
    # tal vez entendí mal el enunciado.
    if ((prom_val_generados >= 300 or prom_val_generados <= 320) and temp_ref != 0):
        print("El horno se encuentra en una temperatura correcta")




