'''
Un salón dispone de 20 puestos numerados del 1 al 20. Desarrolla un programa que permita
gestionar las reservas mediante el siguiente menú:
• 1. Reservar puesto
• 2. Cancelar reserva
• 3. Mostrar puestos disponibles
• 4. Mostrar puestos reservados
• 5. Salir
El programa debe validar que el número del puesto esté entre 1 y 20, que no se pueda reservar un
puesto que ya esté ocupado y que no se pueda cancelar una reserva que no exista. Crea funciones
independientes para reservar, cancelar y consultar puestos.

Datos de entrada:
• Opción del menú (int)
• Número de puesto (int)
Datos de salida:
• Puestos disponibles
• Puestos reservados
• Mensajes de confirmación o error
Conceptos a aplicar: Listas o conjuntos (set), ciclo while, condicionales, funciones y menú.
'''
puest_disp = set(range(1, 21))
puest_res = set()

def res_puesto(puest_disp, puest_res):

    puest = int(input("Ingrese el número del puesto a reservar (1-20): "))

    if puest < 1 or puest > 20:

        print("Número de puesto inválido. Debe estar entre 1 y 20.")

    elif puest in puest_res:

        print(f"El puesto {puest} ya está reservado.")

    else:
        puest_res.add(puest)

        puest_disp.remove(puest)

        print(f"Puesto {puest} reservado con éxito.")

def canc_res(puest_disp, puest_res):

    puest = int(input("Ingrese el número del puesto a cancelar (1-20): "))

    if puest < 1 or puest > 20:

        print("Número de puesto inválido. Debe estar entre 1 y 20.")

    elif puest not in puest_res:

        print(f"El puesto {puest} no está reservado.")

    else:

        puest_res.remove(puest)

        puest_disp.add(puest)

        print(f"Puesto {puest} cancelado con éxito.")

def most_puest_disp(puest_disp):

    print("Puestos disponibles:", sorted(puest_disp))

def most_puest_res(puest_res):

    print("Puestos reservados:", sorted(puest_res))

while True:

    opc = int(input("Elija una opción del menú:\n" \
    "1. Reservar puesto\n" \
    "2. Cancelar reserva\n" \
    "3. Mostrar puestos disponibles\n" \
    "4. Mostrar puestos reservados\n" \
    "5. Salir\n"))

    if opc == 1:

        res_puesto(puest_disp, puest_res)

    elif opc == 2:

        canc_res(puest_disp, puest_res)

    elif opc == 3:

        most_puest_disp(puest_disp)

    elif opc == 4:

        most_puest_res(puest_res)

    elif opc == 5:
        
        print("Saliendo del programa.")
        break
    else:

        print("Opción inválida. Por favor, elija una opción del 1 al 5.")






