"""
Este script está pensado para su ejecución dentro de la ventana de python de ArcGIS Pro
"""

# Define the input table and gdb path
in_table = "Municipios_spain"
gdb_path = r"C:\Proyectos\UME\NuevoVisorAlertas\RegistroAlertasD1.gdb"

# Create a set to hold unique provincia names
provincias = set()

# Use a SearchCursor to iterate through the table and collect unique provincia names
with arcpy.da.SearchCursor(in_table, ["Municipios_spain_AddSpatialJoin.nameunit"]) as cursor:
    for row in cursor:
        provincias.add(row[0])

# Loop through each unique provincia name to export data
for provincia in provincias:
    out_table_name = f"Dominio_{provincia.replace(' ', '_').replace('/', '_')}"
    out_table_path = f"{gdb_path}\\{out_table_name}"

    where_clause = f"Municipios_spain_AddSpatialJoin.nameunit = '{provincia}'"
    arcpy.conversion.ExportFeatures(
    in_features="Municipios_spain",
    out_features=out_table_path,
    where_clause=where_clause,
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='inspireid "INSPIREID" true true false 24 Text 0 0,First,#,Municipios_spain,Municipios_spain.inspireid,0,24;country "COUNTRY" true true false 2 Text 0 0,First,#,Municipios_spain,Municipios_spain.country,0,2;natlev "NATLEV" true true false 128 Text 0 0,First,#,Municipios_spain,Municipios_spain.natlev,0,128;natlevname "NATLEVNAME" true true false 254 Text 0 0,First,#,Municipios_spain,Municipios_spain.natlevname,0,254;natcode "NATCODE" true true false 32 Text 0 0,First,#,Municipios_spain,Municipios_spain.natcode,0,32;codnut3 "CODNUT3" true true false 16 Text 0 0,First,#,Municipios_spain,Municipios_spain.codnut3,0,16;OBJECTID "OBJECTID" false true false 4 Long 0 9,First,#,Municipios_spain,Municipios_spain_AddSpatialJoin.OBJECTID,-1,-1;Join_Count "Join_Count" true true false 4 Long 0 0,First,#,Municipios_spain,Municipios_spain_AddSpatialJoin.Join_Count,-1,-1;TARGET_FID "TARGET_FID" true true false 4 Long 0 0,First,#,Municipios_spain,Municipios_spain_AddSpatialJoin.TARGET_FID,-1,-1;qu_nombre_cmt "QU_nombre_cmt" true true false 15 Text 0 0,First,#,Municipios_spain,Municipios_spain_AddSpatialJoin.qu_nombre_cmt,0,15;nameunit "NAMEUNIT" true true false 50 Text 0 0,First,#,Municipios_spain,Municipios_spain_AddSpatialJoin.nameunit,0,50;fecha_hora_desactivacion "Fecha y hora de desactivación" true true false 8 Date 0 0,First,#,Municipios_spain,Municipios_spain_AddSpatialJoin.fecha_hora_desactivacion,-1,-1;fecha_hora_descenso_nivel "Fecha y hora de descenso de nivel" true true false 8 Date 0 0,First,#,Municipios_spain,Municipios_spain_AddSpatialJoin.fecha_hora_descenso_nivel,-1,-1;codnut1 "codnut1" true true false 15 Text 0 0,First,#,Municipios_spain,Municipios_spain_AddSpatialJoin.codnut1,0,15;codnut2 "codnut2" true true false 15 Text 0 0,First,#,Municipios_spain,Municipios_spain_AddSpatialJoin.codnut2,0,15;cod_prov "Cod_Prov" true true false 15 Text 0 0,First,#,Municipios_spain,Municipios_spain_AddSpatialJoin.cod_prov,0,15;cod_ccaa "Cod_CCAA" true true false 15 Text 0 0,First,#,Municipios_spain,Municipios_spain_AddSpatialJoin.cod_ccaa,0,15;created_user "created_user" true true false 50 Text 0 0,First,#,Municipios_spain,Municipios_spain_AddSpatialJoin.created_user,0,50;created_date "created_date" true true false 8 Date 0 0,First,#,Municipios_spain,Municipios_spain_AddSpatialJoin.created_date,-1,-1;last_edited_user "last_edited_user" true true false 50 Text 0 0,First,#,Municipios_spain,Municipios_spain_AddSpatialJoin.last_edited_user,0,50;last_edited_date "last_edited_date" true true false 8 Date 0 0,First,#,Municipios_spain,Municipios_spain_AddSpatialJoin.last_edited_date,-1,-1;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,Municipios_spain,Municipios_spain_AddSpatialJoin.Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0,First,#,Municipios_spain,Municipios_spain_AddSpatialJoin.Shape_Area,-1,-1;nameunit "NAMEUNIT" true true false 128 Text 0 0,First,#,Municipios_spain,Municipios_spain.nameunit,0,128;codnut1 "CODNUT1" true true false 16 Text 0 0,First,#,Municipios_spain,Municipios_spain.codnut1,0,16;codnut2 "CODNUT2" true true false 16 Text 0 0,First,#,Municipios_spain,Municipios_spain.codnut2,0,16;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,Municipios_spain,Municipios_spain.Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0,First,#,Municipios_spain,Municipios_spain.Shape_Area,-1,-1',
    sort_field=None
)
