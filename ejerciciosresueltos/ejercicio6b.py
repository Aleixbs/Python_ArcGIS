"""
b. Desarrolle un algoritmo que le permita determinar de una lista de números:
b.1. ¿Cuántos están entre el 50 y 75, ambos inclusive?
b.2. ¿Cuántos mayores de 80?
b.3. ¿Cuántos menores de 30?
El algoritmo debe finalizar cuando n (el total de números de la lista), sea igual a 0.
"""
def classificacion():
    numeros = []
    ListA = []
    ListB = []
    ListC = []
    for n in range(1,101):
        numeros.append(n)
        if n > 49 and n < 76:
            ListA.append(n)
        elif n > 80:
            ListB.append(n)
        elif n < 30:
            ListC.append(n)
    else:
        print(0, "Se ha acabado la lista")

    print("Hay ",len(ListA),"números entre 50 y 75 incluidos, en la lista ", ListA)
    print("Hay ",len(ListB), "número mayores de 80 en la lista ", ListB)
    print("Hay ",len(ListC), "números menores de 30 en la lista ", ListC)
classificacion()
