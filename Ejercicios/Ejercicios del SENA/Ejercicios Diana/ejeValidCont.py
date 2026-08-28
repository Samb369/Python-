# Diseña un algoritmo que solicite una contraseña al usuario y la valide contra una contraseña predefinida. Si la contraseña ingresada es incorrecta, 
# debe volver a solicitarla hasta un máximo de tres intentos. 
# Datos de entrada: Contraseña (str) Datos de salida: Mensaje de acceso concedido o denegado 


def validadorCont():

    for c in range(0, 4):

        contIng = input("Escribé la contraseña para acceder: ")

        if contIng == "Sam123":
            
            print("Acceso Concedido")
            break

        else: 

            print("Acceso Denegado")

print("PROGRAMA VALIDADOR DE CONTRASEÑA\n")

validadorCont()

print("PROGRAMA TERMINADO")
