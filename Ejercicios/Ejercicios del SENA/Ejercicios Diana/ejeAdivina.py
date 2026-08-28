#El programa debe generar un número aleatorio entre 1 y 100, 
# y permitir que el usuario lo adivine. 
# Después de cada intento, debe indicar si el número ingresado es mayor o menor al generado. 
# El juego termina cuando el usuario acierta. 
# Datos de entrada: Número ingresado por el usuario (int) Datos de salida: 
# Mensaje de orientación ("Mayor", "Menor", "¡Correcto!") 

import random

def numAleat():

    numAl = random.randint(1, 100)

    while True:

        numIng = int(input("Ingresa un número entre el 1 y el 100: \n"))

        if numIng < 1 or numIng > 100:

            print("Número Inválido\n")

        elif numIng == numAl:

            print("¡Correcto!\n")
            print("Saliendo del programa...\n")

            break

        elif numIng < numAl:

            print("El número aleatorio es mayor\n")

        elif numIng > numAl:

            print("El número aleatorio es menor\n")


print("***PROGRAMA ADIVINA EL NÚMERO***\n")

numAleat()

print("***PROGRAMA TERMINADO***\n")
