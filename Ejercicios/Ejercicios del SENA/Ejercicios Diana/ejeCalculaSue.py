# Un trabajador recibe un sueldo base y, si trabaja más de 40 horas a la semana, 
# recibe una bonificación del 50% sobre las horas extras trabajadas. Diseña un algoritmo que calcule el sueldo total del trabajador. 
# Datos de entrada: Sueldo base (float) Horas trabajadas (int) Pago por hora (float) Datos de salida: Sueldo total (float) 


def calculaSueldo(sueldB, horasT, valorH):
    
    if horasT <= 40:

        valHorTra = horasT * valorH
        sueldoT = sueldB + valHorTra
        return sueldoT
    else:

        valHorTra = horasT * valorH
        horasBon = valHorTra+(valHorTra * 0.5)
        sueldoT = sueldB + horasBon
        return sueldoT

print("PROGRAMA CALCULA SUELDO\n")

sueldB = float(input("Ingrese el sueldo base: \n"))
horasT = float(input("Ingrese las horas trabajadas: \n"))
valorH = float(input("Ingrese el pago por hora: \n"))

sueldoTotal = calculaSueldo(sueldB, horasT, valorH)

print("El sueldo total del trabajador es:", sueldoTotal)
