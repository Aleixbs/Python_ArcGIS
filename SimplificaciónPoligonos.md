# Cómo simplificar polígonos en ArcGIS Pro

https://support.esri.com/en-us/knowledge-base/how-to-reduce-the-number-of-polygon-vertices-in-arcgis-000028143


![image](https://github.com/Aleixbs/Python_ArcGIS/assets/84009394/e4b1d4aa-0ffc-486f-b258-ecc2790f31c7)



HOW TO

Reduce the number of polygon vertices in ArcGIS Pro
Summary
Polygons represent the features of an area on the map. A polygon feature can sometimes contain an excessive number of vertices, and this can cause performance issues such as increase in data size, resulting in longer data loading time. This may also consume more credits when publishing in ArcGIS Online.

In ArcGIS Pro, existing tools with different functionalities and parameters can be used to reduce the number of vertices.

The table below describes the tools that can be used to reduce the number of polygon vertices.

 
Tool	Generalize	Simplify Polygon	Simplify Shared Edges
Definition	Simplifies the input features using a specified maximum offset tolerance	Simplifies the polygon features while preserving the shape	Simplifies the edges of input features while maintaining the topological relationship with edges shared with other features
Input	A line or polygon feature layer	A polygon feature layer	Multiple line or polygon feature layers
Output	Modifies the input feature	Creates a new output	Modifies the input and shared edges features
Method	The Douglas-Peucker simplification algorithm	Five simplification algorithm options	Five simplification algorithm options
Preferences	Best for beginners, as only two parameters must be specified	
Best used to simplify a polygon feature
More parameters can be configured
Best used when inputting multiple features with shared edges
More parameters can be configured
Toolbox	Editing	Cartography	Cartography
In this article, an island polygon feature with 653 vertices is used as the example to demonstrate the functionalities of the tools.

A polygon feature layer with attribute table displaying 653 vertices on ArcGIS Pro.
Note:
The workflows provided apply to ArcGIS Pro 3.0 and above, and may or may not work in ArcGIS Pro 2.x due to changes to the user interface. Refer to ArcGIS Pro: Migration from ArcGIS Pro 2.x to 3.0 for more information on the changes in ArcGIS Pro 3.0.
Procedure
Note:
The Generalize, Simplify Polygon and Simplify Shared Edges tools require an ArcGIS Desktop Standard or Advanced license.
Note:
The Generalize and Simplify Shared Edges tools change the input data permanently. To enable undo, toggle the Enable Undo option on in the tool's geoprocessing pane.
Using the Generalize tool
Open the ArcGIS Pro project.
In the Geoprocessing pane, search for and select Generalize (Editing Tools).
In the Generalize pane, configure the Parameters tab.
For Input Features, select the polygon feature layer from the drop-down list. In this example, 'Pangkor' is selected.
For Tolerance, specify the maximum allowable offset that dictates the degree of simplification. The higher the value, the more simplified the output data. In this example, the tolerance value is set to 1,000 meters.
Click Run.
The Generalize geoprocessing pane.
The map displays the number of vertices reduced using the Generalize tool. To count the vertices, refer to How To: Count the vertices for line or polygon features in ArcGIS Pro.

A polygon feature layer with attribute table displaying 7 vertices on ArcGIS Pro.
Using the Simplify Polygon tool
Open the ArcGIS Pro project.
In the Geoprocessing pane, search for and select Simplify Polygon (Cartography Tools).
In the Simplify Polygon pane, configure the Parameters tab.
For Input Features, select the polygon feature layer from the drop-down menu.
For Output Feature Class, leave the parameter at default, or rename it if necessary.
For Simplification Algorithm, select one of the options from the drop-down list depending on how the algorithm removes the insignificant vertices. The result differs depending on the simplification algorithm used. In this example, Retain effective areas (Visvalingan-Whyatt) is selected. This method uses the identified triangles of effective area to guide the removal of vertices.
For Simplification Tolerance, set a value to determine the degree of simplification. In this example, the value is set to 1,000 meters.
If necessary, specify the Minimum Area and Input Barrier Layers parameters.
Click Run.
The Simplify Polygon geoprocessing pane.
The map displays the number of vertices reduced using the Simplify Polygon tool.

A polygon feature layer with attribute table displaying 10 vertices on ArcGIS Pro.
Using the Simplify Shared Edges tool
Open the ArcGIS Pro project.
In the Geoprocessing pane, search for and select Simplify Shared Edges (Cartography Tools).
In the Simplify Shared Edges pane, configure the Parameters tab.
For Input Features, select the polygon feature layer from the drop-down list. To simplify more than one feature layer, select another feature layer from the second drop-down list.
For Simplification Algorithm, select one of the options from the drop-down list. In this example, Retain weighted areas (Zhou-Jones) is selected. This method uses the weighted triangles of effective area, measured by comparing the flatness, skewness, and convexity of each area to guide the removal of vertices.
For Simplification Tolerance, set a value to determine the degree of simplification. In this example, the value is set to 1,000 meters.
For Shared Edge Features, select the feature that shares the edge with the input feature layer. In this example, the Beach feature layer is selected.
If necessary, specify the Minimum Area and Input Barrier Layers parameters.
Click Run.
The Simplify Shared Edge geoprocessing pane.
The map displays the number of vertices reduced using the Simplify Shared Edges tool.

A polygon feature layer with attribute table displaying 35 vertices on ArcGIS Pro.
Article ID:000028143

Software:
ArcGIS Pro 3 0
ArcGIS Pro 2 8 x
ArcGIS Pro 2 x
