import arcpy
import os

# declaramos que está permitido sobreescribir el resultado
#arcpy.env.overwriteOutput = True

# Decretamos el espacio dónde se encuentra la gdb

miGDB = r"C:\EsriTraining\Arcpy\Datos_Clase\DatosClase\Madrid.gdb"
GDBResultados = r"C:\EsriTraining\Arcpy\Datos_Clase\Resultados3.gdb"

# Para algunas funciones de Lista es necesario haber declarado el workspace TAMBIÉN HACE MÁS COMODO EL TRABAJO

arcpy.env.workspace = miGDB

# Lista entidad GDB con la función List de featureClases "ListFeatureClasses"

listaFC = arcpy.ListFeatureClasses()

for fc in listaFC:

    listaCampos = arcpy.ListFields(fc)
    print("\n" + fc + "\n")
    for campo in listaCampos:   # devuelve un objecto cada iteración de la clase field

        print("campo: {} de tipo {}".format(campo.name, campo.type))



