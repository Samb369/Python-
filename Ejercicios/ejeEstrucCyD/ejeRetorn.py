# 1. Desarrolla una función en Python que reciba un número flotante
#  y retorne su valor absoluto, su doble y su mitad. Datos de entrada: 
# Número (float) Datos de salida: Absoluto (float) Doble (float) Mitad (float) 


def RetorN(num):

    if num < 0:
        numAbs = num * -1
    else:
        numAbs = num
    numD = num * 2

    numM = num / 2
    return numAbs, numD, numM

print("PROGRAMA QUE RETORNA VALORES DE UN NÚMERO")

num = float(input("Ingrese un número: "))

numAbs, numD, numM = RetorN(num)

print("El valor absoluto es: ", numAbs)
print("El doble es: ", numD) 
print("La mitad es: ", numM)
print("PROGRAMA FINALIZADO")