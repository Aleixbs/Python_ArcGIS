#Una compañía de helados ha creado un código para
#que se le introduzca el saber del helado y
#automáticamente indique el precio:
def price(sabor):
    if sabor == "Chocolate":
        precio = 1.99
    else:
        precio = 2.49
    return precio

Choco = price(input())
print(Choco)

#Respecto al ejercicio anterior, ¿qué se mostrará por pantalla con
#las siguientes instrucciones?

#a. print(precio(‘banana’))    ---- 2.49
#b. print(precio(‘chocolate’)) ---- 1.99
#c. print(precio(‘vainilla’))  ---- 2.49