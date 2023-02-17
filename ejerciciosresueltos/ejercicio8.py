"""
Desarrolle un algoritmo que permita leer dos números y ordenarlos de menor a mayor, si es el caso.
"""

A = int(input("A: "))
B = int(input("B: "))
Temporal = 0
orden = []

if A < B:
    Temporal = A
    orden.append(A)
    orden.append(B)
else:
    Temporal = B
    orden.append(B)
    orden.append(A)

print("El menor es: ", Temporal)
print("El orden es: ", orden)