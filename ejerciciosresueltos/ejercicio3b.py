"""
Desarrolle un algoritmo que realice la sumatoria de los números enteros pares comprendidos entre el 1
y el 100, es decir, 2 + 4 + 6 +…. + 100. El programa deberá imprimir los números en cuestión y
finalmente su sumatoria
"""
N = 0
Suma = 0

def suma_mul2(N,Suma):
    list = []
    for i in range(1,101):
       if i % 2 == 0:
           list.append(i)
    print(list)
    x = sum(list)
    print(x)

suma_mul2(N,Suma)