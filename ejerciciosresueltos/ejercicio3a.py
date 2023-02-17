"""
Desarrolle un algoritmo que realice la sumatoria de los números enteros múltiplos de 5, comprendidos
entre el 1 y el 100, es decir, 5 + 10 + 15 +…. + 100. El programa deberá imprimir los números en
cuestión y finalmente su sumatoria
"""

N = 0
Suma = 0

def suma_mul5(N,Suma):
    list = []
    for i in range(1,101):
       if i % 5 == 0:
           list.append(i)
    print(list)
    x = sum(list)
    print(x)

suma_mul5(N,Suma)