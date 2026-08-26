# Diseña un programa que simule un cajero automático. 
# Se debe ingresar un saldo inicial y luego permitir realizar depósitos y retiros hasta que el usuario decida salir. 
# Si un retiro excede el saldo disponible, debe mostrar un mensaje de error. 
# Datos de entrada: Saldo inicial (float) Opciones: Depositar, Retirar, Salir Datos de salida: Saldo actualizado (float) 


def cajeroAuto(saldIni):

    while True:

        opcEle = int(input("Elija una de las siguientes opciones: \n" \
        "1. Depositar saldo \n" \
        "2. Retirar saldo \n" \
        "3. Salir \n"))

        if opcEle == 1:

            saldDep = float(input("Ingresé la cantidad de saldo a depositar: \n"))

            saldIni = saldDep + saldIni

            print(f"El saldo depositado es {saldDep}, saldo actual es {saldIni}")

        elif opcEle == 2:

            saldRet = float(input("Ingresé la cantidad de saldo a retirar: \n"))

            saldIni = saldIni - saldRet

            print(f"El saldo retirado es {saldRet}, el saldo actual es {saldIni}")

        elif opcEle == 3:

            print("Programa finalizando...\n")
            break

        else:

            print("Error: vuelva a intentarlo.\n")


print("***PROGRAMA CAJERO AUTOMÁTICO***\n")

saldIni = float(input("Ingresé un saldo inicial: \n"))

cajeroAuto(saldIni)

print("***PROGRAMA TERMINADO***\n")

        