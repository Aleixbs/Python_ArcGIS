# Escribe la línea de código que falta de forma que el programa
# pregunte por el nombre, hasta que se escriba Carlos.
"""
carlos = "Carlos"
print("Escribe tu nombre: ")
nombre = input()
while nombre != carlos:
    print(nombre + " no eres " + carlos + ", " + "sólo puedes avanzar si eres " + carlos)
    break
else:
    print("¡Hola Carlos!")
"""
carlos = "Carlos"
# Se repite el bloque de codigo hasta que explicitamente se corta con (break)
while True:
    # Le demanda al usuario que escriba su nombre
    print("Escribe tu nombre, no se aceptará cualquier otro nombre que no sea Carlos:")
    # Recoje el input tecleado por el usuario y lo asigna cómo una string (el operador lower() convierte el input de la variable en minusculas
    nombre = str(input()).lower()
    # Se crea un condicional el cuál actuará mientras el input no sea igual a Carlos y repetirá el bloque
    # Con el .casefold() se convierte el string en non case sensitive (o sea que se puede usar con mayus o minus.
    if nombre != carlos.casefold():
        print("No eres Carlos")
    # Si es Carlos en este caso se romperá el bloque de codigo
    else:
        print("¡Hola Carlos!")
        break