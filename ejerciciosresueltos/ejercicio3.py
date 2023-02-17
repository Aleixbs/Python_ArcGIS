"""
Desarrolle un algoritmo que realice la sumatoria de los números enteros comprendidos entre el 1 y el 10,
es decir, 1 + 2 + 3 + …. + 10.
"""

N = 0
Suma = 0

def sumatorio(N,Suma):
    list = []
    for i in range(10):
        list.append(i + 1)
    a = sum(list)
    print(list)
    print(a)
sumatorio(N,Suma)
