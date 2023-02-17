'''
El siguiente código de ejemplo muestra cómo obtener las propiedades de datos y verificar una extensión
'''

import arcpy

# print True if exists
print(arcpy.Exists(r"C:\Users\usuario\Desktop\ESRI documentos clase\Modulo 3\5.Desarrollo de scripts con Arcpy\Datos_documentacion\PYTS\Data\CountyData.gdb\ParcelPts"))

# print Spatial Reference
spatial_Reference = arcpy.Describe(r"C:\Users\usuario\Desktop\ESRI documentos clase\Modulo 3\5.Desarrollo de scripts con Arcpy\Datos_documentacion\PYTS\Data\CountyData.gdb\ParcelPts").spatialReference
print(spatial_Reference.name)

# print Available
print(arcpy.CheckExtension("spatial"))

arcpy.CheckOutExtension("spatial")