"""
Desarrolle un algoritmo que permita determinar el área y volumen de un cilindro dado su radio (R) y
altura (H).
"""
import math
R = 0
H = 0
Pi = math.pi
def area_cilindro(R,H,Pi):
    Pi = math.pi
    R = int(input("Define el radio: "))
    H = int(input("Define la altura: "))
    R2 = R **2
    List = []
    Vol = Pi * R2 * H
    Area = 2 * Pi * R * H + 2 * Pi + R2
    List.append(Vol)
    List.append(Area)
    print(List)
area_cilindro(R,H,Pi)