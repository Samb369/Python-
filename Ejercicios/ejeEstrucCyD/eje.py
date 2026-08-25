# Diseña un algoritmo que permita ingresar las edades de "n" personas y luego calcule: 
# La edad promedio La edad mínima La edad máxima Datos de entrada: 
# Lista de edades (int) Datos de salida: Edad promedio (float) Edad mínima (int) Edad máxima (int) 


import statistics

def estadisEdad(edadN):

    if edadN > 0:

        for c in range(0, edadN):

            contEdas = float(input("¿Cuáles son las edades de las personas?"))

            listEdas = []
            listEdas.append(contEdas)

        edadP = statistics.mean(listEdas)

        edadMi = min(listEdas)

        edadMa = max(listEdas)
        return edadP, edadMi, edadMa
        
    else:

        print("No hay edades de personas para calcular")

print("PROGRAMA ESTADÍSTICO DE EDADES\n")

edadN = int(input("¿Cuántas edades quieres ingresar?\n"))

edadP, edadMi, edadMa = estadisEdad(edadN)

print("La edad promedio del grupo de personas es ", edadP)
print("La edad minima del grupo de personas es ", edadMi)
print("La edad máxima del grupo de personas es ", edadMa)
print("PROGRAMA TERMINADO")
        

