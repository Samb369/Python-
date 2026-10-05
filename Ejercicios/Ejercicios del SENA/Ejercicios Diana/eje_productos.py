'''
Desarrolla un programa que permita registrar varios productos de una tienda. Para cada producto
se debe almacenar su nombre, precio y cantidad disponible.

El programa debe permitir ingresar n productos y, al finalizar, mostrar:
• Todos los productos registrados.
• El producto con mayor cantidad disponible.
• El producto con menor cantidad disponible.
• El valor total del inventario.
• Una alerta para los productos cuya cantidad sea menor a 5 unidades.
Crea al menos una función que calcule el valor total de un producto (precio × cantidad).
Datos de entrada:
• Nombre del producto (str)
• Precio (float)
• Cantidad (int)
Datos de salida:
• Lista de productos
• Producto con mayor existencia
• Producto con menor existencia
• Valor total del inventario (float)
• Productos con bajo inventario
Conceptos a aplicar: Listas, diccionarios, funciones, ciclo for y condicionales.
'''


num_produc = int(input("¿Cuántos productos desea registrar?\n"))

list_produc = [] 

for p in range(num_produc):

    nom_produc = str(input("Ingresa el nombre del producto.\n"))
    
    pre_produc = float(input("Ingresa el precio del producto.\n"))
    
    can_produc = int(input("Ingresa la cantidad de productos.\n"))

    list_produc.append({
        "Nombre": nom_produc,
        "Precio": pre_produc,
        "Cantidad": can_produc
    })

produc_may = max(list_produc, key=lambda produc: produc["Cantidad"])

produc_min = min(list_produc, key=lambda produc: produc["Cantidad"])


print("Lista de productos: ")
for cont_produc in list_produc:
    print(cont_produc["Nombre"])

print(f"El producto con mayor cantidad es: {produc_may["Nombre"]}")

print(f"El producto con menor cantidad es: {produc_min["Nombre"]}")

def prec_tot():
    return sum(
        prod["Precio"] * prod["Cantidad"]
        for prod in list_produc
    )

print(f"Valor total del inventario: {prec_tot()}")

for produc in list_produc:

    if  produc["Cantidad"] < 5:

        print(f"Esto son los productos con bajas existencia: {produc["Nombre"]}")
        