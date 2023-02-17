"""
Desarrolle un algoritmo que permita leer un valor cualquiera N y escriba si dicho número es par o impar.
"""
N = 0

def parimpar():
    N = int(input())
    if N % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

parimpar()