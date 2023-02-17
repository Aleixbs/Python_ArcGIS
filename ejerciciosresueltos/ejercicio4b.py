"""
b. Desarrollar un algoritmo que calcule el área de un cuadrado.
"""

Lado = 0

def area_cuadrado(Lado):
    Lado = int(input("Define la longitud de los lados del cuadrado: "))
    Area = Lado ** 2
    print(Area)

area_cuadrado(Lado)