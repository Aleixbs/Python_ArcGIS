import arcpy
import os

fcCalles = r"C:\EsriTraining\Arcpy\Datos_Clase\DatosClase\Madrid.gdb\calles"
miDescribe = arcpy.Describe(fcCalles) # objeto de la clase describe (que apunta a la feature class calles)
listaCampos = miDescribe.fields
aliasCampos = []
nameCampos = []
tipoCampos = []

print("El sistema de coordenadas proyectadas es: {}".format(miDescribe.spatialReference.name ))  #Se llama a la propiedad name del objeto spatial reference del archivo fcCalles (que se encuentra en miDescibe)
print("El sistema geográfico de coordenadas es: {}".format (miDescribe.spatialReference.GCS.name ))

for campo in listaCampos:
    aliasCampos.append(campo.aliasName)
for campo in listaCampos:
    nameCampos.append(campo.name)
for campo in listaCampos:
    tipoCampos.append(campo.type)

print(listaCampos)
print(aliasCampos)
print(nameCampos)
print(tipoCampos)

for campo in listaCampos:
    print("El campo {} es de tipo {}".format(campo.name,campo.type))

#  hasattr() se pueden obtener información sobre si un objeto presenta una determinada propiedad

if hasattr(miDescribe, "bandCount") == True:
    print("Tiene la propiedad")
else:
    print("No tiene la propiedad")

if hasattr(miDescribe, "name") == True:
    print("Tiene la propiedad")
else:
    print("No tiene la propiedad")