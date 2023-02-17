
"""
Crear un campo en la tabla de parques con el nombre EmpresaConcesionaria
Con un cursor crearemos una condicion que nos relleneraá los campos según la siguiente condicion:
La empresa concesionaria
"""

import arcpy
import os

fcParques = r"C:\EsriTraining\Arcpy\Datos_Clase\DatosClase\Madrid.gdb\Parques"
nombreCampo = "EmpresaConcesionaria"
ListaCampos = ["POLYGON_NM", "Shape_Area", nombreCampo]
LimiteParquesMedianos = 50000
LimiteParquesGrandes = 200000

arcpy.AddField_management(fcParques, nombreCampo, "TEXT" )

with arcpy.da.UpdateCursor(fcParques, ListaCampos ) as miUpdateCursor:
    for entidad in miUpdateCursor:
        if entidad[1] <= LimiteParquesMedianos:
            entidad[2] = "Empresa1"
        elif entidad[1] > LimiteParquesMedianos and entidad[1] < LimiteParquesGrandes:
            entidad[2] = "Empresa2"
        elif entidad[1] > LimiteParquesGrandes:
            entidad[2] = "Empresa3"

        miUpdateCursor.updateRow(entidad)

        print(entidad[0])




