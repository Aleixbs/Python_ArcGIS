"""
Determinar la hipotenusa de un triángulo rectángulo conocidas las longitudes de sus dos catetos.
Desarrolle el algoritmo correspondiente

a: ¿Qué falta en este algoritmo? ¿ Qué errores presenta?
En el algoritmo falta detallar bien el teorema de pitágoras (la fórmula tendría que ser con los catetos al cuadrado)
"""
import math

CatA = 0
CatB = 0

def hipotenusa(CatA,CatB):
    CatA = int(input("Define el 1r cateto: "))
    CatB = int(input("Define el 2n cateto: "))
    HipC = math.sqrt(CatA **2 + CatB **2)
    print("El valor de la hipotenusa es: ", HipC)

hipotenusa(CatA,CatB)