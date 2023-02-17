"""
Realiza el mismo algoritmo utilizando Mientras (While);
"""
def califications():
    n = int(input())
    while n != 0 and n < 21:
        if n >= 19:
            nuevanota = "A"
            break
        elif n >= 16 and n <= 18:
            nuevanota = "B"
            break
        elif n >= 13 and n <= 15:
            nuevanota = "C"
            break
        elif n >= 10 and n <= 12:
            nuevanota = "D"
            break
        elif n >= 1 and n <= 9:
            nuevanota = "E"
            break
    else:
        nuevanota = "0"
        print("Has sacado un zero")


    print(nuevanota)

califications()

