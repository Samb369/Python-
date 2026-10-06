'''
Desarrolla un programa que simule el proceso de compra de una pequeña tienda. Inicialmente
debe existir un diccionario con algunos productos y sus precios, por ejemplo:

productos = {
"Arroz": 4500,
"Leche": 3800,
"Pan": 2500,
"Huevos": 12000
}

El usuario podrá seleccionar productos y cantidades hasta que indique que desea finalizar la compra.
El programa debe utilizar funciones para consultar si un producto existe, calcular el subtotal de cada
producto, calcular el total de la compra y aplicar un descuento del 10 % si la compra supera los
$100.000. Finalmente, debe mostrar un resumen de la compra con los productos, cantidades,
subtotales, descuento y total a pagar.
Datos de entrada:
• Producto (str)
• Cantidad (int)
Datos de salida:
• Productos comprados
• Subtotal por producto (float)
• Subtotal de la compra (float)
• Descuento (float)
• Total a pagar (float)
Conceptos a aplicar: Diccionarios, listas, funciones, ciclo while, condicionales y acumuladores.
'''

from math import prod


producs = {
    "CARNE": 25000,
    "POLLO": 15000,
    "PESCADO": 20000,
    "VERDURAS": 8000,
    "AGUACATE": 12000
}

carrit = []

def cons_produc(prod):

    return prod in producs

def subtot_produc(prec, cant):

    return prec * cant

def tot_comp(carrit):

    tot = 0

    for art in carrit:

        tot += art["subtotal"]

    return tot  

def apli_desc(tot):

    if tot > 100000:

        descuento = tot * 0.10

    else:

        descuento = 0

    return descuento

def most_resu(carrit, tot, desc):

    print("\nRESUMEN COMPRA")

    for art in carrit:

        print(f"{art['producto']}: {art['cantidad']} unidades x ${art['precio']} = ${art['subtotal']}")

    print(f"Subtotal compra: {tot}")

    print(f"Descuento: {desc}")

    print(f"Total a pagar: {tot - desc}")

while True:

    prod_eleg = input("Ingrese el producto que desea comprar (Carne, Pollo, Pescado, Verduras, Aguacate): ").upper()

    if not cons_produc(prod_eleg):

        print("No tenemos ese producto.")
        continue

    cant_prod = int(input(f"Ingrese la cantidad de {prod_eleg}: "))

    if cant_prod <= 0:

        print("La cantidad debe ser mayor a cero.")
        continue

    subtotal = subtot_produc(producs[prod_eleg], cant_prod)

    carrit.append({

        "producto": prod_eleg,
        "cantidad": cant_prod,
        "precio": producs[prod_eleg],
        "subtotal": subtotal
    })


    opcion = input("¿Desea agregar otro producto? (S/N): ").upper()

    if opcion == "N":
        break

tot = tot_comp(carrit)
desc = apli_desc(tot)
most_resu(carrit, tot, desc)