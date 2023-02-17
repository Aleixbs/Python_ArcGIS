import arcpy

fcEntrada = arcpy.GetParameterAsText(0)
fcSalida = arcpy.GetParameterAsText(1)
radioBuffer = arcpy.GetParameterAsText(2)
lineSide = arcpy.GetParameterAsText(3)
opcionDisolver = arcpy.GetParameterAsText(4)


arcpy.Buffer_analysis(fcEntrada,fcSalida, str(radioBuffer) + " Meters", lineSide, dissolve_option = opcionDisolver )

arcpy.AddMessage("BIEN HECHO")
