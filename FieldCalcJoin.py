import arcpy

# Set the workspace (adjust this to your file's location)
arcpy.env.workspace = r'C:\Carpeta\NombreGDB.gdb'

# Specify the names of your tables
target_table = 'NombreFC o Tabla'  # The table where the field will be calculated
join_table = 'NombreFC o Tabla'  # The table containing the values for calculation

# Specify the common field used to join the tables
join_field_target = 'NAMEUNIT'
join_field_join = 'NAMEUNIT'

# Specify the field to calculate and the field from which to get the calculation values
field_to_calculate = 'cod_prov'  # Field in target_table to be calculated
calculation_field = f'{join_table}.{join_field_join}'  # Field in join_table used for calculation

# Join the tables
arcpy.AddJoin_management(target_table, join_field_target, join_table, join_field_join, 'KEEP_COMMON')

# Calculate the field (example calculation)
# Adjust the expression based on your calculation requirements
arcpy.CalculateField_management(target_table, field_to_calculate, f"!{calculation_field}!", "PYTHON3")

# Optionally, remove the join if no longer needed
arcpy.RemoveJoin_management(target_table)
