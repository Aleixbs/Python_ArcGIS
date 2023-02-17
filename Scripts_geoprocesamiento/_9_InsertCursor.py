"""
Search cursor para recorrer el csv y adquirir los datos que vamos a introducir a los campos de la clase de entidad de Hoteles como una nueva entidad
Insert cursor para introducir las nuevas entidades (filas con geometría)

"""
import arcpy

fcHoteles = r"C:\EsriTraining\Arcpy\Datos_Clase\DatosClase\Madrid.gdb\hoteles"
csvActualizacion = r"C:\EsriTraining\Arcpy\Datos_Clase\DatosClase\HotelesActualizacion.csv"

listaCamposHoteles = ["ETIQUETA", "Adress", "Stars", "SHAPE@XY"]
listaCamposCSV = ["NOMBRE", "DIRECCION", "ESTRELLAS", "COORDENADAX", "COORDENADAY"]

with arcpy.da.SearchCursor(csvActualizacion, listaCamposCSV ) as  SCursorCSV:

    with arcpy.da.InsertCursor(fcHoteles, listaCamposHoteles) as ICursorHoteles:   #Este cursor será el que tendrá la estructura de lista de campos preferida

        for filaCSV in SCursorCSV:    # recorremos los campos de la fila del CSV

            nuevaEntidadHoteles = [filaCSV[0], filaCSV[1], filaCSV[2], (filaCSV[3], filaCSV[4])]  # el TOKEN SHAPE@XY siempre se rellena con una tupla

            ICursorHoteles.insertRow(nuevaEntidadHoteles)

print("Completed")






