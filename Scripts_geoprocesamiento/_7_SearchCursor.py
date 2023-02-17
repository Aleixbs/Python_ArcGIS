import arcpy
import os

# declaramos que está permitido sobreescribir el resultado
#arcpy.env.overwriteOutput = True

# Decretamos el espacio dónde se encuentra la gdb

miGDB = r"C:\EsriTraining\Arcpy\Datos_Clase\DatosClase\Madrid.gdb\hoteles"
claseEntidad = r"C:\EsriTraining\Arcpy\Datos_Clase\DatosClase\Madrid.gdb\hoteles"

listadoCampos = ["ETIQUETA", "Stars", "Adress","SHAPE@XY"]

# El cursor es una serie de filas de la tabla objetivo
miSearchCursor = arcpy.da.SearchCursor(claseEntidad, listadoCampos)   # El cursor es cómo si fuera una lista de filas (una tabla de manera virtual desde la cuál podemos acceder a las filas y a sus valores


with arcpy.da.SearchCursor(claseEntidad, listadoCampos) as miSearchCursor:
    for fila in miSearchCursor:
        print("El {} tiene {} estrellas y se encuentra en la dirección: {} Con CoorX:{} y CoorY: {}".format(fila[0], fila[1], fila[2],round(fila[3][0],2), round(fila[3][1],2)))                     # se tiene que indicar la posición del elemento a printear según el indice de la lista de campos de entrada




