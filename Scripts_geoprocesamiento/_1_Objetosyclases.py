"""
Cómo funcionan las clases, objetos y métodos
"""
class Coche():                  #Se crea una clase con los objetos que la definen
    velocidad = 0
    color = "desconocido"
    motor = "gasolina"
    marca = ""
    fechaMatriculacion = ""

    def acelerar(self, nuevaVelocidad):         # metodo + (parámetros)
        self.velocidad = nuevaVelocidad         # self apuntará a la clase y velocidad será el objeto de la clase que modificaremos

    def calificacionEnergetica(self):
        if self.fechaMatriculacion < 2000:
            return "A"
        elif self.fechaMatriculacion > 2000 and self.motor == "gasolina":
            return "B"
        elif self.motor == "híbrido":
            return "ECO"
        elif self.motor == "eléctrico":
            return "0"
        else:
            return "desconocido"



miCoche = Coche()

print(miCoche.motor)

print(miCoche.marca)

miCoche.marca = "Volkswagen"

print(miCoche.marca)

print(miCoche.velocidad)

miCoche.acelerar(100) # llamamos el método acelerar de la clase y modificamos el parámetro velocidad mediante la funcion

print(miCoche.velocidad)

miCoche.fechaMatriculacion = 2006
                                        # Mediante el método calificacion Energetica se puede decretar la etiqueta ecológica
print(miCoche.calificacionEnergetica()) # Expected output = B (fechamatriculacion = 2006 y motor = gasolina)

miCoche.motor = "híbrido"

print(miCoche.calificacionEnergetica()) # Expected ouput = ECO (fechamatriculación = 2006 y motor = híbrido