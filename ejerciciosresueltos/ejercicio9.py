"""
Desarrolle un algoritmo que permita leer un valor entero positivo N y determinar si es primo o no.
    a. ¿Qué falta en este algoritmo? ¿ Qué errores presenta? ---> fixed
        En el algoritmo falta una lista para almacenar los números divisores para determinar si es primo o no(cuando solo son 2 es primo, si hay más, no)
"""
n = int(input("N: "))
factoriales = []
    for i in range(1,n+1):
        if n % i == 0:
            factoriales.append(i)
    if len(factoriales) <= 2:
        print("Es un número primo")
    else:
        print("No es un número primo")
    print(factoriales)


List = [1, 4, 5, 20, 65, 74, 23, 12, 62, 90, 52, 34, 45, 26, 11, 33, 17, 13, 14, 21, 22, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
    for i in range(List[1], n + 1):
        if n % i == 0:
            factoriales.append(i)
    if len(factoriales) <= 2:
        print("Es un número primo")
    else:
        print("No es un número primo")
    print(factoriales)