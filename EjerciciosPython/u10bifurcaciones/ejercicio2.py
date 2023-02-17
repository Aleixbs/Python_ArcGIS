# Completa el código siguiente para que diga “Coge un pastel”
# siempre y cuando se introduzca Pastel. De lo contrario haz
# que le ofrezca una Galleta.

print("¿Cual es tu comida favorita?")
comida = input()
if comida == "pastel":
    print("Coge " + "un " + comida)
else:
    print("Coge una Galleta" )

