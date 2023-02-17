"""
Ejercicio 2.
Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las variables A, B y C
respectivamente. El algoritmo debe imprimir cual es el mayor y cual es el menor. Recuerde constatar que
los tres valores introducidos por el teclado sean valores distintos. Presente un mensaje de alerta en caso de
que se detecte la introducción de valores iguales.

Parte a. Es este algoritmo la solución perfecta al ejercicio anterior? Razone su respuesta.
            Si podría ser una solución perfecta del ejercicio anterior, ahorra pasos y genera un resultado valido
Parte b. De ser necesario ¿qué cambios deberá realizar? Indíquelos.
            Se ha cambiado el statement (variable) control para que no imprima dos veces el resultado cuando se ejecuta el while
"""

A = 0
B = 0
C = 0
control = "False"
def comparacion_a_tres_may():
    print("Introduce los valores de las siguientes variables:")
    A = input("A: ")
    B = input("B: ")
    C = input("C: ")
    while A == B and C == B:
        print("Los números deben ser distintos")
        A = input("A: ")
        B = input("B: ")
        C = input("C: ")
        if B < A and A > C:
            if control == "True":
                print("A es el mayor.")
        elif B > A and B > C:
            if control == "True":
                print("B es el mayor.")
        else:
            if control == "True":
                print("C es el mayor")

    if control == "False":
        if B < A and A > C:
            print("A es el mayor.")
        elif B > A and B > C:
            print("B es el mayor.")
        else:
            print("C es el mayor")

comparacion_a_tres_may()



