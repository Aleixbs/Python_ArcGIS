import arcpy
import random

# Define your calc() function
def calc():
    sampleList = [1, 2]
    randomList = random.choices(sampleList, weights=(9, 1), k=1)
    if randomList[0] == 1:
        return 'No'
    elif randomList[0] == 2:
        return 'Si'
    else:
        return 'No'

# Specify the path to your feature class
feature_class = r"C:\carpeta\NombreGDB.gdb\NombreFC"

# Get a list of field names in the feature class
field_names = [field.name for field in arcpy.ListFields(feature_class)]

# Iterate over the fields and update them if they don't have values
with arcpy.da.UpdateCursor(feature_class, field_names) as cursor:
    for row in cursor:
        for i, field_value in enumerate(row):
            if field_value is None:
                # Apply the calc() function to fill in the None values
                row[i] = calc()
        cursor.updateRow(row)
Traceback (most recent call last):
  File "<string>", line 28, in <module>
RuntimeError: The value type is incompatible with the field type. [ObjectID_1]
import arcpy
import random

# Define your calc() function
def calc():
    sampleList = [1, 2]
    randomList = random.choices(sampleList, weights=(9, 1), k=1)
    if randomList[0] == 1:
        return 'No'
    elif randomList[0] == 2:
        return 'Si'
    else:
        return 'No'

# Specify the path to your feature class
feature_class = r"C:\carpeta\NombreGDB.gdb\NombreFC"

# Get a list of field names and their data types in the feature class
field_info = [(field.name, field.type) for field in arcpy.ListFields(feature_class)]

# Create a list of field names that can be updated
updateable_fields = [field[0] for field in field_info if field[0] != "ObjectID"]

# Iterate over the rows and fields to update
with arcpy.da.UpdateCursor(feature_class, updateable_fields) as cursor:
    for row in cursor:
        for i, field_value in enumerate(row):
            field_name = updateable_fields[i]
            field_data_type = [info[1] for info in field_info if info[0] == field_name][0]

            # Check if the field value is None and its data type is compatible with the calc() output
            if field_value is None and field_data_type in [u'String', u'Double', u'SmallInteger']:
                # Apply the calc() function to fill in the None values
                row[i] = calc()
        cursor.updateRow(row)
