import arcpy

# Set the workspace
arcpy.env.workspace = r'C:\Proyectos\UME\NuevoVisorAlertas\VisorAlertasV2.gdb'

# Define the feature class
feature_class = 'AlertasPlanesEspeciales'

# List all fields in the feature class
fields = arcpy.ListFields(feature_class)

# Filter out fields to update: Only 'TEXT' fields are considered for length change
text_fields = [field for field in fields if field.type == 'String' and field.length > 15]

# Process each 'TEXT' field to change its length to 15
for field in text_fields:
    old_field_name = field.name
    temp_field_name = f"Temp_{old_field_name}"  # Temporary field name

    # Ensure temp_field_name does not exceed the field name length limit, typically 64 characters for most databases
    temp_field_name = (temp_field_name[:60] + "_tmp") if len(temp_field_name) > 63 else temp_field_name

    # Step 1: Add a temporary field with the desired new length
    arcpy.AddField_management(feature_class, temp_field_name, 'TEXT', field_length=15)
    
    # Step 2: Copy data from the old field to the temporary field
    expression = f"!{old_field_name}!"
    arcpy.CalculateField_management(feature_class, temp_field_name, expression, "PYTHON3")
    
    # Step 3: Delete the old field
    arcpy.DeleteField_management(feature_class, old_field_name)
    
    # Step 4: Add a new field with the original name and desired length
    arcpy.AddField_management(feature_class, old_field_name, 'TEXT', field_length=15)
    
    # Step 5: Copy data from the temporary field to the new field
    arcpy.CalculateField_management(feature_class, old_field_name, f"!{temp_field_name}!", "PYTHON3")
    
    # Step 6: Delete the temporary field
    arcpy.DeleteField_management(feature_class, temp_field_name)
