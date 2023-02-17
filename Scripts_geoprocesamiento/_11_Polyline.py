"""
Se recorren cada uno de los puntos con un SearchCursor se van a capturar las coordenadas del TOken y se va a generar un array desde el cuál se generará El objeto Polyline
"""
import arcpy
import os

arcpy.env.overwriteOutput = True

shpPuntos = r"C:\EsriTraining\Arcpy\Datos_Clase\DatosClase\Puntos_caminos_retiro.shp"
shpPuntos2 = r"C:\EsriTraining\Arcpy\Datos_Clase\DatosClase\Madrid.gdb\PuntosOrden"
shpPuntosSalida = r"C:\EsriTraining\Arcpy\Datos_Clase\DatosClase\LineaRetiro3.shp"


objetoPoint = arcpy.Point()
miArray = arcpy.Array()
CRS = arcpy.SpatialReference(25830)

with arcpy.da.SearchCursor(shpPuntos2, ["SHAPE@XY"], sql_clause = (None, "ORDER BY Orden") ) as miSCursor:
    for entidad in miSCursor:

        objetoPoint.X = entidad[0][0]
        objetoPoint.Y = entidad[0][1]

        miArray.add(objetoPoint)


#miPolilinea = arcpy.Polyline(miArray, CRS)
miPoligono = arcpy.Polygon(miArray, CRS)

arcpy.CopyFeatures_management(miPoligono, shpPuntosSalida)


print("FIN")



