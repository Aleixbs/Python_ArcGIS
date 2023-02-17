"""
Ejercicio 2. Parte C
Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las variables A, B, y C
respectivamente. El algoritmo debe indicar cual es el menor. Asumiendo que los tres valores
introducidos por el teclado son valores distintos.
"""

A = 0
B = 0
C = 0
control = "False"
def comparacion_a_tres_men():
    print("Introduce los valores de las siguientes variables:")
    A = input("A: ")
    B = input("B: ")
    C = input("C: ")
    while A == B and C == B:
        print("Los números deben ser distintos")
        A = input("A: ")
        B = input("B: ")
        C = input("C: ")
        if control == "True":
            if A < B and A < C:
                print("A es el menor.")
            elif B < A and B < C:
                print("B es el menor.")
            else:
                print("C es el menor.")

    if control == "False":
        if A < B and A < C:
            print("A es el menor.")
        elif B < A and B < C:
            print("B es el menor.")
        else:
            print("C es el menor.")

comparacion_a_tres_men()



