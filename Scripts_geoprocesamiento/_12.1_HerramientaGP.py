
# Importamos los módulos necesarios
import arcpy


# Declaramos las variables
fcTiendas = arcpy.GetParameterAsText(0)
gdbOut = arcpy.GetParameterAsText(1)
selectTiendas = arcpy.GetParameterAsText(2)
facturacionMinima = arcpy.GetParameterAsText(3)
bufferTiendas = arcpy.GetParameterAsText(4)
distanciaBuffer = arcpy.GetParameterAsText(5)
fcCalles = arcpy.GetParameterAsText(6)
clipCalles = arcpy.GetParameterAsText(7)

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