'''
Ejercicio 3.1: Leer y actualizar valores en una clase de
entidad
Documentación Arcpy pág 114
Autor: Aleix
Coding : utf-8
'''

# importar modulos

import arcpy

# set environments y workspace
#arcpy.env.workspace = r"C:\Data\Datos_documentacion\PYTS\Data\CountyData.gdb"
arcpy.env.overwriteOutput = True

# declarar variables
#fc = 'ParcelPts' la clase de entidad sobre la que ejecutaremos el cursor
fc = r"C:\Data\Datos_documentacion\PYTS\Data\CountyData.gdb\ParcelPts"
# lista de campos necesarios para la operación dentro de la clase de entidad
campos = ['SquFoot', 'TaxValue', 'PriceSquFt']

# Crear un cursor para actualizar el campo sq/Ft price
# Necesitamos el tamaño de la parcela, el valor total y el campo priceSqft

# Crearemos una lista con el Update Cursor que hará referencia ala fc y a los campos dentro de esta que necesitamos
with arcpy.da.UpdateCursor(fc,campos) as miUpdateCursor:

# bucle for que recorrerá la fc y me generará una tabla virtual con los tres campos con el orden de la lista
    for campo in miUpdateCursor:
        campo[2] = campo[1] / campo[0]
        miUpdateCursor.updateRow(campo)

print("Calculados los valores en el campo PriceSquFT")

# Crear un SearchCursor para acceder al ID de la parcela, el nombre y numero de telefono del dueño y el precio
# Crearemos una lista con la lista de los campos que necesitamos
campos2 = ["Parcel_ID", "Owner_Name", "Phone_Number", "PriceSquFt", "SHAPE@XY"]

# Crearemos una expresión SQL para limitar la búsqueda a las propiedades con un valor menor a 90$/sqft
whereClauseSQL = '"PriceSquFt" <= 90'

# Crearemos una lista de las parcelas para almacenar los valores resultantes de la selección
parcelasValidas = ["Parcel_ID, Owner_Name, Phone_Number, PriceSquFt, Xcoords, Ycoords"]

# Creamos el Search Cursor para su uso
with arcpy.da.SearchCursor(fc, campos2, whereClauseSQL) as miSearchCursor:
    for row in miSearchCursor:
        textoCampo = "{},{},{},{},{},{}".format(row[0],row[1],row[2],row[3],str(row[4][0]),str(row[4][1]))
        parcelasValidas.append(textoCampo)

print("Creamos la lista de valores validos")

# Escribir los valores de las parcelos que cumplen con los requisitos en un CSV
# Con \n conseguimos que cada elemento se incorpore como una nueva linia en el Csv
textoCuerpo = '\n'.join(parcelasValidas)

# Abrimos un archivo al cuál escribiremos los valores deseados con la función open (sino existe se creará un archivo con el nombre)
archivoCSV = open(r"C:\Data\Datos_documentacion\PYTS\AssessmentParcelsXY.csv","w")

archivoCSV.write(textoCuerpo)

archivoCSV.close()

print("Script Completado")
