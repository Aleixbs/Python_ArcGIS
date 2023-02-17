#Crea una función llamada dibuja_triangulo de manera que
#automáticamente dibuje un triangulo.

# aqui se importa turtle cómo forma de tortuga en el cursor
from turtle import*
shape('turtle')
# en esta linea se estipula la funcion con la variable medida y un loop for
# con un rango de 3 para que dibuje el triangulo
def dibuja_triangulo(medida = 150):
    for n in range(3):
        # cuando avance la tortuga dibujará una linea con el valor de medida en px (la base del triangulo)
        forward(medida)
        # cuando gire a la izquierda la linea que dibujará es de 120px
        # (y luego volvera a girar a la izquierda con otra de 120px) para completar el triangulo
        left(120)
# en esta linea estamos llamando a la función para que se ejecute en la consola de turtle python graphics
dibuja_triangulo()
# esta funcion la usamos para que se quede la ventana emergente congelada y podamos apreciar el resultado
done()
