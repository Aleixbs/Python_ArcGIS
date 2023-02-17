import arcpy
import os

fcCalles = r"C:\EsriTraining\Arcpy\Datos_Clase\DatosClase\Madrid.gdb\calles"
carpetaGDB = r"C:\EsriTraining\Arcpy\Datos_Clase"
nombreGDB = r"Resultados3.gdb"    # El .gdb!!!!! CUIDADO!!!
nombrecopiaCalles = r"fcCopia"

arcpy.env.overwriteOutput = True

miDescribe = arcpy.Describe(fcCalles) #Creamos un objeto de la clase describe que almacenamos dentro de una variable

print("el tipo de dato de la FC ES: {} y la ruta de acceso es {}".format(miDescribe.dataType, miDescribe.path))
print("la clase de entidad {} tiene un tipo de geometría de {}".format(miDescribe.name, miDescribe.shapeType))


arcpy.CreateFileGDB_management(carpetaGDB, nombreGDB)
                                                        # El workspace nos permite seleccionar una gdb predeterminada por lo tanto no hará falta declarar la ruta cada vez
arcpy.env.workspace = os.path.join(carpetaGDB, nombreGDB)

# Decratamos
if miDescribe.shapeType == "Point":
    arcpy.CopyFeatures_management(fcCalles, miDescribe.name + "_Copia" )
    arcpy.AddXY_management(miDescribe.name + "_Copia")

elif miDescribe.shapeType == "Polygon" or miDescribe.shapeType == "Polyline":
    arcpy.FeatureToPoint_management(fcCalles, miDescribe.name + "_Punto")
    arcpy.AddXY_management(miDescribe.name + "_Punto")
else:
    pass

print("fin")

