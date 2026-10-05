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
produc = {} 

for p in range(num_produc):

    nom_produc = str(input("Ingresa el nombre del producto.\n"))
    produc["Nombre"] = nom_produc

    pre_produc = float(input("Ingresa el precio del producto.\n"))
    produc["Precio"] = pre_produc

    can_produc = int(input("Ingresa la cantidad de productos.\n"))
    produc["Cantidad"] = can_produc

    list_produc.append(produc)

print(produc["Nombre"])
print(produc)