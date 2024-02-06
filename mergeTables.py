import arcpy
import pandas as pd

# Path to your feature class
gdb = r"C:\ModelodatosAlertas.gdb"
arcpy.env.workspace = gdb

fcList = arcpy.ListFeatureClasses()

fcMergeList = [fc for fc in fcList if not any(substring in fc.lower() for substring in ['_icono', '_iconos'])]

def get_prefix(table_path):
    # This function extracts a 2-letter code from the table name.
    # Adjust this logic based on your table naming conventions and requirements.
    # Example: if your table_path is "C:/data/geodatabase.gdb/TableName", this will return "TA"
    
    table_name = table_path.split('/')[-1]  # Adjust this line if necessary to properly extract the table name
    
    names = {
        'Alertas_inundaciones': 'IU', 
        'Alertas_Terremotos' : 'TE', 
        'Alertas_Nevadas' : 'NV', 
        'Alertas_Incendios' : 'IC',
        'Alertas_Nuclear' : 'NU',
        'Alertas_Medioabiente' : 'MA', 
        'Alertas_R_Biologico' : 'RB', 
        'Alertas_Quimicas' : 'QU'
    }
    
    prefix = names.get(table_name, 'Code not found')
    
    #prefix = table_name[:2].upper()  # Using the first two letters as the prefix, converted to uppercase
    return prefix


def table_to_df(table_path):
    
    prefix = get_prefix(table_path)
    
    # List all fields in the table
    fields = [field.name for field in arcpy.ListFields(table_path)]
    
    prefixed_fields = [f"{prefix}_{field}" if field not in ['OBJECTID', 'SHAPE', 'Shape', 'Shape_Length', 'Shape_Area', 'fecha_hora_descenso_nivel', 'fecha_hora_desactivacion', 'globalid', 'created_user', 'created_date', 'last_edited_user', 'edited_date', 'cod_prov', 'cod_ccaa', 'nameunit'] else field for field in fields]
    
    # Use a search cursor to read the table rows
    data = [row for row in arcpy.da.SearchCursor(table_path, fields)]
    
    # Convert to a pandas DataFrame
    df = pd.DataFrame(data, columns=prefixed_fields)
    return df

dfList = []
for table in fcMergeList:
    
    full_table_path = f"{gdb}/{table}"
    
    df = table_to_df(full_table_path)
    
    dfList.append(df)


# Concatenate them into a single DataFrame
concatenated_df = pd.concat(dfList, ignore_index=True)
concatenated_df.info()

concatenated_df.to_excel(r'C:\alertas.xlsx')
    
