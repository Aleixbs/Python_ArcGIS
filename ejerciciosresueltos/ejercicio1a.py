"""
Ejercicio No: 1
Parte a
Desarrolle un algoritmo que permita leer dos valores distintos, determinar cual de los dos valores es el
mayor y escribirlo.
"""

A = 0
B = 0
# inicializamos la funcion
def introducir():
    # pedimos los valores A y B
    print("Introduzca dos valores")
    A = input("Valor A: ")
    B = input("Valor B: ")
    # empezamos un while para aplicar un condicional cuando los valores sean iguales
    while A == B:
        # Si los valores son iguales Se piden que los valores sean distintos
        # El loop while se sigue aplicando
        print("Introduzca dos valores distintos: ")
        A = input("Valor A: ")
        B = input("Valor B: ")
        # Se aplica un condicional sobre que si siguen siendo iguales se aplique este mensaje
        # el loop while se sigue aplicando
        if A == B:
            print("Siguen siendo iguales")
        #Cuando los valores son distintos se aplica otra condicion que evalua si a es mayor que b
        elif A > B:
            print("A es mayor que B")
        # SI A no es mayor a B entonces B es mayor que A
        else:
            print("B es mayor que A")
    # Si se han introducido los valores distintos desde un inicio la función evalua si A es mayor que B
    if A > B:
        print("A es mayor que B")
    # En caso contrario B será mayor a A
    else:
        print("B es mayor que A")
introducir()


