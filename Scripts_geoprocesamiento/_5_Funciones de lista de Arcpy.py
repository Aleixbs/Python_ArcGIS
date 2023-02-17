import arcpy
import os


arcpy.env.overwriteOutput = True
# Decretamos el espacio dónde se encuentra la gdb

miGDB = r"C:\EsriTraining\Arcpy\Datos_Clase\DatosClase\Madrid.gdb"
GDBResultados = r"C:\EsriTraining\Arcpy\Datos_Clase\Resultados3.gdb"

# Para algunas funciones de Lista es necesario haber declarado el workspace TAMBIÉN HACE MÁS COMODO EL TRABAJO

arcpy.env.workspace = r"C:\EsriTraining\Arcpy\Datos_Clase\DatosClase\Madrid.gdb"

# Lista entidad GDB con la función List de featureClases "ListFeatureClasses"

listaFC = arcpy.ListFeatureClasses()

# Crear un objeto de la clase spatialReference para usarlo más adelante
CRS = arcpy.SpatialReference(25830)

"""
for fc in listaFC:
  
    arcpy.CopyFeatures_management(fc, os.path.join(GDBResultados + fc) + "_copia")
    print(fc)
"""
print ("fin")

# Creamos un describe.

"""    
for fc in listaFC:
    miDescribe = arcpy.Describe(fc)
    if miDescribe.shapeType == "Polyline":
        arcpy.CopyFeatures_management(fc, os.path.join(GDBResultados, fc) + "_polyline")
        print(fc)
"""
# WKID :23030 ED 50 PROYECTAR  // WKID :25830 ETRS 89 COPIAR
for fc in listaFC:
    miDescribe = arcpy.Describe(fc)
    if miDescribe.spatialReference.factoryCode == 25830:
        arcpy.CopyFeatures_management(fc, os.path.join(GDBResultados, fc) + "_ETRS89")
    elif miDescribe.spatialReference.factoryCode == 23030:
        arcpy.Project_management(fc, os.path.join(GDBResultados, fc) + "_ED50toETRS89", CRS, "ED_1950_To_ETRS_1989_12_NTv2_Spain_v2")
    print(fc)
print("fin")
