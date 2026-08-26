# Un estudiante tiene tres notas en su curso. 
# Cada nota tiene un porcentaje diferente: 
# Nota 1: 30% Nota 2: 30% Nota 3: 40% 
# El programa debe calcular la nota final y determinar si el estudiante aprueba (nota final ≥ 3.0) o reprueba.
#  Datos de entrada: Nota1 (float) Nota2 (float) Nota3 (float) Datos de salida: Nota final (float) Estado (str: "Aprobado" o "Reprobado") 


def calcuNota(not1, not2, not3):

    not1 = not1 * 0.3
    not2 = not2 * 0.3
    not3 = not3 * 0.4

    notFin = (not1 + not2 + not3)/3.0

    print(f"La nota final del estudiante es: {notFin}")
    
    if notFin >= 3.0:

        print("El estudiante ha aprobado")

    else:

        print("El estudiante ha desaprobado")


print("***PROGRAMA CALCULA NOTAS***\n")

not1 = float(input("Ingresa la nota 1: \n"))
not2 = float(input("Ingresa la nota 2: \n"))
not3 = float(input("Ingresa la nota 3: \n"))

notaFin = calcuNota(not1, not2, not3)

print(notaFin)
