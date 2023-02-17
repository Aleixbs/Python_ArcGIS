"""
Título: Práctica Navidad Arcpy --- Ejecución Merge mediante archivos obtenidos del IGN ---
Materia: Desarrollo de Scripts con Arcpy
Autor: Aleix Batlle Sureda
Código: UTF-8
Fecha: 08/01/2023
Versión: 1.0
"""
# Importar módulos

import arcpy
import os

# Directorio principal de las carpetas de datos

directorioPrincipal = r"C:\EsriTraining\Arcpy\PRACTICA_PYTHON_NAVIDAD\Datos"

# Creación de la GDB de ficheros

carpetaProyecto = r"C:\EsriTraining\Arcpy\Prueba_Final\PruebaOpcionalArcpy"     # Directorio de creación de GDB
nombreGDB = r"ResultadosPruebaFinal.gdb"                                            # Nombre GDB salida

arcpy.CreateFileGDB_management(carpetaProyecto,nombreGDB)                       # Creación GDB ficheros
GDBsalida = os.path.join(carpetaProyecto,nombreGDB)

# Configuración environment

arcpy.env.overwriteOutput = True
arcpy.env.workspace = os.path.join(carpetaProyecto,nombreGDB)                   # Configuración GDB salida predeterminada

# Lista Shp de las carpetas de Datos

listaCarpetas = os.listdir(directorioPrincipal)
listaSHP = []

for carpeta in listaCarpetas:

    carpetasDatos = os.path.join(directorioPrincipal,carpeta)

    archivos = os.listdir(carpetasDatos)

    for shape in archivos:

        if r".shp" in shape:

            listaSHP.append(shape)

# Lista de nombres únicos de los archivos

listaSHPunicos = [*set(listaSHP)]

# Función con la cuál se obtienen las rutas de cada archivo unitario

def encontrar_Carpeta(directorioCarpetas,nombreArchivo):

    listaRutaCarpetas = []

    for carpetas in os.listdir(directorioCarpetas):

        rutaCarpetas = os.path.join(directorioCarpetas,carpetas)

        if os.path.exists(os.path.join(rutaCarpetas,nombreArchivo)) == True:

            listaRutaCarpetas.append(os.path.join(rutaCarpetas,nombreArchivo))

    return listaRutaCarpetas

# Iteración a partir de la cuál se ejecutará el merge con las rutas de los archivos en la GDB de Salida

for nombreSHP in listaSHPunicos:

    mergeInputs = encontrar_Carpeta(directorioPrincipal,nombreSHP)

    mergeOutputs = os.path.join(GDBsalida, os.path.splitext(nombreSHP)[0])

    arcpy.management.Merge(mergeInputs,mergeOutputs)

