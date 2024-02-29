import arcpy
# Set the workspace (adjust the path as necessary)
#arcpy.env.workspace = "C:/data"

# Define your layer
layer = 'PEUME_Alertas'

# Getting the subtypes
subtypes = arcpy.da.ListSubtypes(layer)

for stcode, stdict in list(subtypes.items()):
    # Using the subtype name as the domain name
    domain_name = stdict['Name']

    for stkey in list(stdict.keys()):
        if stkey == "FieldValues":

            fields = stdict[stkey]
            for field, fieldvals in list(fields.items()):

                # Check if the field name contains 'localidad_principal'
                if 'localidad_principal' in field:
                    # Attempt to assign the domain to this field for the current subtype
                    print('Assigning domain to field...{field}')
                    try:
                        arcpy.AssignDomainToField_management(layer, field, domain_name, stcode)
                        print(f"Assigned '{domain_name}' domain to field '{field}' for subtype code '{stcode}'.")
                    except Exception as e:
                        print(f"Error assigning domain to field '{field}': {e}")

        else:
            print(f"{stkey}: {stdict[stkey]}")
