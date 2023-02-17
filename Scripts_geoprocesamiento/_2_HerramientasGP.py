# módulos que usaremos
import arcpy
import os

# Propiedad que permite sobreescribir todos los datos en general  --- Vigila que las capas no estén cargadas al mapa
arcpy.env.overwriteOutput = True

# Variables que utilizaremos
fcTiendas = r"C:\EsriTraining\Arcpy\Datos_Clase\DatosClase\Madrid.gdb\TIENDAS"
fcCalles = r"C:\EsriTraining\Arcpy\Datos_Clase\DatosClase\Madrid.gdb\calles"
carpetaResultados = r"C:\EsriTraining\Arcpy\Datos_Clase"
nombreGDB = "Resultados2.gdb"
queryTiendas = "VENTAS > 500000"
distanciaBuffer = 500

# función dentro del módulo path dentro del módulo OS (concatena 2 textos mediante una barra)
gdbResultados = os.path.join(carpetaResultados,nombreGDB)

# Establecemos un entorno de trabajo predeterminado dónde se almacenarán todos los outputs de las funciones
arcpy.env.workspace = gdbResultados

# Herramienta que crea un nueva GDB File dónde se van a guardar todos los resultados
arcpy.CreateFileGDB_management(carpetaResultados, nombreGDB)

# Herramienta de selección la cuál creará una nueva entidad a partir de la selección # que se almacenará en la dirección de la carpeta de resutlados
arcpy.Select_analysis(fcTiendas, "SeleccionTiendas", queryTiendas)

# Herramienta para ejecutar un Buffer
arcpy.Buffer_analysis( "SeleccionTiendas", "BufferTiendas", str(distanciaBuffer) + " Meters" )

# Herramienta clip
arcpy.Clip_analysis(fcCalles,"BufferTiendas", "CallesPublicidad")

print("FIN")
# Si salen errores puede ser que sea porque tenemos abierto el IDE y ArcGIS Pro a la vez

