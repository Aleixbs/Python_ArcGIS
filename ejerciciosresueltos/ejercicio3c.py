"""
Desarrolle un algoritmo que lea los primeros 300 números enteros y determine cuántos de ellos son
impares; al final deberá indicar su sumatoria
"""
N = 0
Suma = 0

def num_impar(N,Suma):
    list = []
    for i in range(1,301):
        x = i % 2 == 0
        if x == 0:
            pass
        else:
            list.append(i)
    impares = len(list)
    sumatorio = sum(list)
    print(impares)
    print(list)
    print(sumatorio)

num_impar(N,Suma)