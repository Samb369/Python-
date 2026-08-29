# Desarrolla un programa que permita registrar y almacenar en un diccionario la información 
# de estudiantes, donde la clave sea el número de identificación y el valor sea un nombre. El 
# programa debe permitir agregar, modificar y eliminar estudiantes del diccionario.


print("\n***PROGRAMA DICCIONARIO***\n")

estu = {}

while True:

    opcEli = int(input("Elija una opción: \n1. Agregar estudiante\n2. Modificar estudiante\n3. Eliminar estudiante\n4. Salir\n"))

    if opcEli == 1:

        idEstu = int(input("Ingresé el número de identificación: \n"))

        estu[idEstu] = ""

        nomEstu = input("Ingresé en nombre del estudiante: \n")

        estu[idEstu] = nomEstu

        print(f"Diccionario de estudiantes: {estu}\n")

    elif opcEli == 2:

        clavMod = int(input("Ingresé el ID que quiere modificar: \n"))

        valMod = input("Ingresé el nuevo nombre del ID: \n ")

        estu[clavMod] = valMod

        print(f"Diccionario de estudiantes: {estu}")

    elif opcEli == 3:

        clavEli = int(input("Ingresé el ID a eliminar: \n"))

        if clavEli not in estu:

            print("No existe este ID.")

        else: 

            del estu[clavEli]
            
            print("El número de identificación ha sido eliminado.")
            
            print(f"Diccionario de esudiante: {estu}")
            
    elif opcEli == 4:

        print("Saliendo del programa...\n")
        break
        
print("***PROGRAMA TERMINADO***\n")
        
