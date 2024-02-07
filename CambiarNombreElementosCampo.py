import arcpy

# Set the workspace (update the path to your ArcGIS Pro project's workspace)
arcpy.env.workspace = r'C:\NombreCarpeta\NombreGDB.gdb'

# Define the feature class
feature_class = 'AlertasProvincias'

# Define the old field name, the temporary field name, and the new field specifications
old_field_name = 'QU_nombre_cmt'
temp_field_name = 'TempFieldName'  # Ensure this name is unique within the feature class
new_field_type = 'TEXT'  # For example, 'TEXT', 'LONG', 'FLOAT', 'DOUBLE', etc.
new_field_length = 15  # Only applicable for text fields

# Step 1: Add a temporary field and copy the old field data to it
arcpy.AddField_management(feature_class, temp_field_name, new_field_type, field_length=new_field_length)
expression = f"!{old_field_name}!"
arcpy.CalculateField_management(feature_class, temp_field_name, expression, "PYTHON3")

# Delete the old field
arcpy.DeleteField_management(feature_class, old_field_name)

# Step 2: Add a new field with the original name and desired specifications
arcpy.AddField_management(feature_class, old_field_name, new_field_type, field_length=new_field_length)

# Step 3: Copy data from the temporary field to the new field
expression = f"!{temp_field_name}!"
arcpy.CalculateField_management(feature_class, old_field_name, expression, "PYTHON3")

# Step 4: Delete the temporary field
arcpy.DeleteField_management(feature_class, temp_field_name)
