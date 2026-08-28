# El programa debe permitir al usuario agregar productos a una lista de compras, eliminarlos y mostrar la lista actualizada hasta que decida salir. 
# Opciones del menú: 1. Agregar producto 2. Eliminar producto 3. Mostrar lista 4. Salir Datos de entrada: 
# Opción del menú (int) Producto (str) Datos de salida: Lista de compras actualizada (list) 


print("\n***PROGRAMA TIENDA***\n")

listProd = []

while True:

    opcEli = int(input("Elija una de las siguientes opciones: \n1. Agregar producto\n2. Eliminar producto\n3. Mostrar producto\n4. Salir\n"))

    if opcEli == 1:

        nomProd = input("Escriba el nombre del producto: \n").upper()

        listProd.append(nomProd)

        print(f"Lista actualizada: {listProd}\n")

    elif opcEli == 2:

        
        eliProd = input(f"¿Cuál producto desea eliminar de la lista {listProd}\n").upper()

        if eliProd not in listProd:

            print("No existe este producto.\n")
            
        else:
        
            listProd.remove(eliProd)

            print(f"Lista actualizada: {listProd}\n")
    
    elif opcEli == 3:

        print(f"Lista actualizada: {listProd}\n")

    elif opcEli == 4:

        print("Saliendo del programa...\n")
        break
        
    else:

        print("ERROR: Vuelva a intentarlo.\n")

print("***PROGRAMA TERMINADO***\n")
