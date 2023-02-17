"""
Constructor de la clase "point". Todas la cualidades de la clase point són de lectura y escritura (se pueden editar)
"""

import arcpy
import os

arcpy.env.overwriteOutput = True

GDBResultados = r"C:\EsriTraining\Arcpy\Datos_Clase\Resultados3.gdb\GeometriasPuntoBuffer"
CRS = arcpy.SpatialReference(25830)

punto1 = arcpy.Point()

print(punto1.X)

punto1.X = 440000
punto1.Y = 4480000

print(punto1)

punto2 = arcpy.Point( 435000, 4485000)

print("FIN")

"""
PointGeometry = [] es una lista que almacena los objetos generados mediante la clase constructor Point y los conecta para formar una forma geométrica
"""

geometriaPunto1 = arcpy.PointGeometry( punto1, CRS )

geometriaPunto2 = arcpy.PointGeometry( punto2, CRS )

listaPG = [geometriaPunto1, geometriaPunto2]


arcpy.Buffer_analysis(listaPG, GDBResultados, "1000 Meters" )

arcpy.CopyFeatures_management(listaPG, GDBResultados)

print("FIN")