'''
Diseña un programa que permita registrar las notas finales de n estudiantes. Para cada estudiante
se almacenará su nombre y nota final.

El programa debe utilizar una función para determinar el estado académico de cada estudiante según
las siguientes condiciones:
• Nota ≥ 4.5: "Excelente"
• Nota ≥ 3.5 y < 4.5: "Bueno"
• Nota ≥ 3.0 y < 3.5: "Aprobado"
• Nota < 3.0: "Reprobado"
Al finalizar, debe mostrar el promedio general del grupo, la cantidad de estudiantes aprobados y
reprobados, el estudiante con mayor nota y el estudiante con menor nota.

Datos de entrada:
• Nombre (str)
• Nota (float)
Datos de salida:
• Promedio (float)
• Estado de cada estudiante (str)
• Cantidad de aprobados y reprobados (int)
• Mayor y menor nota
Conceptos a aplicar: Funciones, listas, diccionarios, condicionales y ciclos.
'''


estudiantes = []

num_not = int(input("¿Cuántas notas vas a ingresar?\n"))

for cont_not in range(num_not):

    nom_est = str(input("Ingresé el nombre del estudiante: \n"))
    not_fin = float(input("Ingresé la nota final del estudiante: \n"))

    estudiantes.append({
        "Nombre": nom_est,
        "Nota Final": not_fin
    })

def estd_not():

    prom_est = sum(estd["Nota Final"] for estd in estudiantes) / len(estudiantes)
    print(f"\nEl promedio general del grupo es: {prom_est}\n")

    for cont_not in estudiantes:


        if cont_not["Nota Final"] >= 4.5:

            print(f"Los estudiantes con nota excelente: {cont_not['Nombre']}")

        elif cont_not["Nota Final"] >= 3.5 and cont_not["Nota Final"] < 4.5:

            print(f"Los estudiantes con nota bueno: {cont_not['Nombre']}")

        elif cont_not["Nota Final"] < 3.5 and cont_not["Nota Final"] >= 3.0:

            print(f"Los estudiantes con nota aprobado: {cont_not['Nombre']}")

        elif cont_not["Nota Final"] < 3.0:

            print(f"Los estudiantes con nota reprobado: {cont_not['Nombre']}")

    for cont_not in estudiantes:

        if cont_not["Nota Final"] < 3.0:

            print(f"Los estudiantes reprobados: ")
            print(f"{cont_not['Nombre']}")

        elif cont_not["Nota Final"] >= 3.0:

            print(f"Los estudiantes aprobados: ")
            print(f"{cont_not['Nombre']}")

estd_not()




