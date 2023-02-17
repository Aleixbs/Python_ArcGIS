"""
Desarrolle un algoritmo que permita convertir calificaciones numéricas, según la siguiente tabla:
A = 19 y 20, B =16, 17 y 18, C = 13, 14 y 15, D = 10, 11 y 12, E = 1 hasta el 9. Se asume que la nota está
comprendida entre 1 y 20
"""

def calificaciones():
    n = int(input("Que nota has sacado entre el 1 y el 20: "))
    a = "Entonces has sacado una "
    if n >= 19:
        nuevanota = "A"
    elif n >= 16 and n <= 18:
        nuevanota = "B"
    elif n >= 13 and n <= 15:
        nuevanota = "C"
    elif n >= 10 and n <=12:
        nuevanota = "D"
    elif n >= 1 and n <= 9:
        nuevanota = "E"
    else:
        print("Has sacado un zero")
    print(a,nuevanota)
calificaciones()
