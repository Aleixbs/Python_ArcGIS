# Cálculo del número de vértices

https://support.esri.com/en-us/knowledge-base/how-to-count-the-vertices-for-line-or-polygon-features-000027446



![image](https://github.com/Aleixbs/Python_ArcGIS/assets/84009394/0ea1a82a-850b-4869-a439-52dafddf480b)


Count the vertices for line or polygon features in ArcGIS Pro
Summary
In some instances, it is necessary to find the number of vertices for each feature in a line or polygon feature class to perform further spatial analysis. This article provides the workflow for the counting of vertices of line or polygon features in ArcGIS Pro.

Procedure
Start the ArcGIS Pro project.
In the Contents pane, browse to and right-click the layer, and click Attribute Table.
In the layer’s attribute table, click Add to add a new field in the table.
![image](https://github.com/Aleixbs/Python_ArcGIS/assets/84009394/dc64859c-2e81-4433-afe3-6af84f31ff75)

Click Add to add a new field to the attribute table.
In the Fields view, name the new field as VxCount and ensure Data Type is set to Long.
On the top ribbon, on the Fields tab, in the Changes group, click Save to save the edits made.
![image](https://github.com/Aleixbs/Python_ArcGIS/assets/84009394/cadb055a-c743-4cf6-bbc0-846bbdf74ff3)

Click the Save button to save the edits.
In the attribute table, right-click the header of the VxCount field, and select Calculate Field.
![image](https://github.com/Aleixbs/Python_ArcGIS/assets/84009394/c1086f78-dcc2-4a22-8876-05696b95e76a)

Select Calculate Field to calculate the number of vertices of the polygon layer.
In the Calculate Field window, ensure the following parameters are specified as follows:
Input Table: The desired layer. In this example, the layer titled BuildingDamage is selected.
Field Name (Existing or New): VxCount.
Expression Type: Python 3.
VxCount =: !shape!.pointcount
Leave other parameters as default.
Click OK to run the tool.
![image](https://github.com/Aleixbs/Python_ArcGIS/assets/84009394/124bd32b-74fa-45d8-b29c-46035c14d2e6)

Specify the tool parameter to calculate the number of vertices of the polygon layer in the Calculate Field window.
The image below shows the number of vertices for the layer titled BuildingDamage displayed in the VxCount field in the attribute table.
![image](https://github.com/Aleixbs/Python_ArcGIS/assets/84009394/10104652-017c-46da-a137-c4ae3db57871)

The number of vertices populated in the VxCount field in the attribute table.
Article ID:000027446

Software:
ArcGIS Pro 2 x
ArcGIS Pro 2 7 x
ArcGIS Pro 2 8 x
