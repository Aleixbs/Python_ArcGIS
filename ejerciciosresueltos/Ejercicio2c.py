"""
Ejercicio 2. Parte d.
Desarrolle un algoritmo que lea cuatro números diferentes y a continuación imprima el mayor de los
cuatro números introducidos y también el menor de ellos.
"""
a = 0
b = 0
c = 0
d = 0
def min_max(a,b,c,d):
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")
    d = input("d: ")
    x = min(a,b,c,d)
    print("El número más pequeños es = ", x)
    y = max(a,b,c,d)
    print("El número más grande es = ",y)

min_max(a,b,c,d)