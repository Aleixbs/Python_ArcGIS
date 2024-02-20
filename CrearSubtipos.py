import arcpy

# Set the workspace (change this to your geodatabase or folder path)
arcpy.env.workspace = r"C:\Proyectos\UME\NuevoVisorAlertas\RegistroAlertasD1.gdb"

# Feature class path
feature_class = "PEUME_Alertas"

# Fields to base subtypes on: code field and description field
subtype_code_field = "cod_Subtype" # This field should ideally contain integer values.
subtype_desc_field = "nameunit"  # This is the field for subtype descriptions.

# Set the subtype field
arcpy.SetSubtypeField_management(feature_class, subtype_code_field)
print(f"Set subtype field: {subtype_code_field}")

# Get unique pairs of code and description values from the fields
unique_pairs = {(row[0], row[1]) for row in arcpy.da.SearchCursor(feature_class, [subtype_code_field, subtype_desc_field]) if row[0] is not None and row[1] is not None}

# Loop through unique pairs and add each as a subtype
for code, description in unique_pairs:
    # Add subtype using code and description
    arcpy.AddSubtype_management(feature_class, code, description)
    print(f"Added subtype: {code} - {description}")
