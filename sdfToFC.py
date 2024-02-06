Bill Chappell 6/2020 bill@gistechsolutions.com

import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import pandas as pd

from arcgis.features import GeoAccessor, GeoSeriesAccessor

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'gray')
canvas1.pack()

def getExcel ():
    global df
    
    filename = askopenfilename(filetypes=[("Excel files", ".xlsx")])

    df = pd.read_excel (filename)

    #To read column names from Excel file.
    #for col in df.columns:
        #print(col)
    
    #Rename column names
    df_new = df.rename(columns={'Pole/Tower Position':'Pole_Tower',
                                'Structure Latitude':'Lat',
                                'Structure Longitude':'Lng',
                                'Child Equipment Type':'Equipment_Type'})
    
    #To check new column names in use.
    #for i in df_new.columns:
        #print(i)

    # replace null values in Lat/Lng fields with Zeros
    df_new["Lat"] = df_new["Lat"].fillna(0)
    df_new["Lng"] = df_new["Lng"].fillna(0)   
                       
    #Using dictionary to convert specific columns to correct field type
    convert_dict = {'Pole_Tower': str,
                    'Lat':float,
                    'Lng':float,
                    'Equipment_Type':str}

    df2fc = df_new.astype(convert_dict) 
    #print(df2fc.dtypes)

    # Converts a Pandas DataFrame into a Spatial DataFrame by providing the X/Y columns.
    #https://developers.arcgis.com/python/api-reference/arcgis.features.toc.html#arcgis.features.SpatialDataFrame.from_xy
    sdf= pd.DataFrame.spatial.from_xy(df=df2fc,
                                      x_column='Lng',
                                      y_column='Lat',
                                      sr=4326)
    # show first 5 records in SDF
    #print(sdf.head())

    #Write a CSV to check progress
    #sdf.to_csv('checkme.txt', sep='\t', index=False)
    
    #converts a SpatialDataFrame to a ShapeFile.
    #sdf.spatial.to_featureclass(location=r"C:\Users\BChappell\temp\test3.shp", overwrite=True)
    
    #converts a SpatialDataFrame to a feature class.
    #https://developers.arcgis.com/python/api-reference/arcgis.features.toc.html?highlight=spatialdataframe#arcgis.features.GeoAccessor.to_featureclass
    sdf.spatial.to_featureclass(location=r"C:\Users\BChappell\temp\test.gdb\TPoles", overwrite=True)

    print("Done")

    
    
browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)

root.mainloop()
