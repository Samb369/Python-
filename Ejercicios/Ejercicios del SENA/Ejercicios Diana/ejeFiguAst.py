# Crea un programa que imprima un triángulo de asteriscos de altura n, donde n es un 
# número ingresado por el usuario.

print("\n***PROGRAMA TRIANGULO***\n")

numAst = int(input("Ingresa un número \n"))

if numAst < 3:

    print("No se puede crear un triangulo de asterico.")

else:

    for s in range(1, numAst, +1):

        print("*" * s)
        
print("***PROGRAMA TERMINADO***\n")
