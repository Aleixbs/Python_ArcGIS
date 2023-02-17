'''
Cuando se trabaja módulos existentes dentro de arcpy como arcpy.sa muchas veces surge la necesidad
de anidar varias funciones y clases en una sola línea de código para realizar una operación, como cuando
se trabaja con la función Raster. La sentencia from-import-* permite simplificar la lectura del código, tal
y como se muestra en el siguiente ejemplo.
'''
import arcpy
from arcpy.sa import *  # importamos spatial analyst
arcpy.sa.Slope()

arcpy.CheckOutExtension("spatial")
arcpy.env.workspace = r"C:\MyData\Myproject.gdb"
raster1 = "Slope"("elevation" ,"DEGREE", 0.3043)
raster2 = "SolarRad"

outRaster = (Raster(raster1)) + (Raster(raster2))