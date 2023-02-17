'''
09/01/2023
Aleix
Scripts Arcpy ---- Herramienta de Geoprocesamiento
code = utf-8
'''
# Importamos los módulos necesarios
import arcpy


# Declaramos las variables
fcTiendas = r"C:\EsriTraining\Arcpy\Datos_Clase\DatosClase\Madrid.gdb\TIENDAS"
selectTiendas = "Tiendas_Select"
gdbOut = r"C:\EsriTraining\Arcpy\Datos_Clase\Resultados.gdb"
facturacionMinima = 500000
bufferTiendas = "Tiendas_Buffer"
distanciaBuffer = 300
fcCalles = r"C:\EsriTraining\Arcpy\Datos_Clase\DatosClase\Madrid.gdb\calles"
clipCalles = "Calles_Clip"

# Nombramos los environtments esto nos ahorra de añadir el path a la gdb de salida
arcpy.env.workspace = gdbOut
arcpy.env.overwriteOutput = True

# Escribimos los pasos de procesamiento del Script y añadimos un mensaje en cada uno de los pasos
arcpy.Select_analysis(fcTiendas, selectTiendas, "VENTAS >" + str(facturacionMinima))

arcpy.AddMessage("Ejecutando la selección de Tiendas")

arcpy.Buffer_analysis(selectTiendas, bufferTiendas, str(distanciaBuffer) + " Meters")

arcpy.AddMessage("Ejecutando el buffer a partir de la seleccion de las Tiendas")

arcpy.Clip_analysis(fcCalles,bufferTiendas,clipCalles)

arcpy.AddMessage("SCRIPT EJECUTADO CON ÉXITO")

print("FIN")