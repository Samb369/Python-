'''
Una tienda desea analizar las ventas realizadas durante una semana. Desarrolla un programa que
permita ingresar las ventas correspondientes a los 7 días de la semana.

Crea funciones para:
• Calcular el total vendido.
• Calcular el promedio diario.
• Determinar el día con mayor venta.
• Determinar el día con menor venta.
Adicionalmente, el programa debe mostrar cuáles días tuvieron ventas superiores al promedio
semanal.
Datos de entrada:
• Ventas de lunes a domingo (float)
Datos de salida:
• Total semanal (float)
• Promedio (float)
• Día de mayor venta
• Día de menor venta
• Días con ventas superiores al promedio
Conceptos a aplicar: Listas, ciclo for, condicionales y funciones.
'''


dia_lun = []
dia_mar = []
dia_mie = []
dia_jue = []
dia_vie = []
dia_sab = []
dia_dom = []

while True:

    opc = input("¿Desea ingresar las ventas de la semana? (S/N): \n").upper()

    if opc == "N":
        break

    elif opc == "S":

        while True:

            vent_lun = float(input("Ingrese las ventas del día lunes: \n"))
            dia_lun.append(vent_lun)

            opcl = str(input("¿Tiene más ventas para ingresar? (S/N): \n")).upper()

            if opcl == "S":
                continue
            elif opcl == "N":

                vent_mar = float(input("Ingrese las ventas del día martes: \n"))
                dia_mar.append(vent_mar)

                opcm = str(input("¿Tiene más ventas para ingresar? (S/N): \n")).upper()

                if opcm == "S":
                    continue

                elif opcm == "N":

                    vent_mie = float(input("Ingrese las ventas del día miércoles: \n"))
                    dia_mie.append(vent_mie)

                    opcmie = str(input("¿Tiene más ventas para ingresar? (S/N): \n")).upper()

                    if opcmie == "S":
                        continue

                    elif opcmie == "N":

                        vent_jue = float(input("Ingrese las ventas del día jueves: \n"))
                        dia_jue.append(vent_jue)

                        opcj = str(input("¿Tiene más ventas para ingresar? (S/N): \n")).upper()

                        if opcj == "S":
                            continue

                        elif opcj == "N":

                            vent_vie = float(input("Ingrese las ventas del día viernes: \n"))
                            dia_vie.append(vent_vie)

                            opcv = str(input("¿Tiene más ventas para ingresar? (S/N): \n")).upper()

                            if opcv == "S":
                                continue

                            elif opcv == "N":

                                vent_sab = float(input("Ingrese las ventas del día sábado: \n"))
                                dia_sab.append(vent_sab)

                                opcs = str(input("¿Tiene más ventas para ingresar? (S/N): \n")).upper()

                                if opcs == "S":
                                    continue

                                elif opcs == "N":

                                    vent_dom = float(input("Ingrese las ventas del día domingo: \n"))
                                    dia_dom.append(vent_dom)

                                    opcd = str(input("¿Tiene más ventas para ingresar? (S/N): \n")).upper()

                                    if opcd == "S":
                                        continue

                                    elif opcd == "N":
                                        break

def tot_vent():

    total_vent = sum(dia_lun) + sum(dia_mar) + sum(dia_mie) + sum(dia_jue) + sum(dia_vie) + sum(dia_sab) + sum(dia_dom)
    print(f"\nEl total semanal es: {total_vent}\n")

    prom_vent = total_vent / 7
    print(f"El promedio diario de ventas: {prom_vent}\n")

    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    vent = [sum(dia_lun), sum(dia_mar), sum(dia_mie), sum(dia_jue), sum(dia_vie), sum(dia_sab), sum(dia_dom)]

    dia_may = dias[vent.index(max(vent))]
    print(f"El día con mayor venta es: {dia_may}\n")

    dia_men = dias[vent.index(min(vent))]
    print(f"El día con menor venta es: {dia_men}\n")

    print("Dias con ventas superiores al promedio:")
    for i in range(len(vent)):
        if vent[i] > prom_vent:
            print(f"{dias[i]}: {vent[i]}")

tot_vent()
