'''
En una geodatabase tenemos varios datasets y en cada dataset tenemos varias clases de entidad.
Definimos para una geodatabase que almacena información sobre el abastecimiento y saneamiento de
una red de agua:
 fileGDB = [ [“Abastecimiento”, [“Estacion de bombeo”, “Tuberia”, “Valvula”]], [“Saneamiento”,
[“Pozos”, “Colectores”]] ]
De este modo, nuestra lista “fileGDB” contiene dos elementos que a su vez son listas.
----------------------------------------------------------------------------------------
implementa un programa que muestre por pantalla el nombre de cada uno de los datasets.
Existe la posibilidad de anidar estructuras, como ya se ha visto anteriormente. En el caso de nuestra
geodatabase de agua, nos solicitan que mostremos no solo el nombre del dataset, sino que, además,
mostremos los nombres de las clases de entidad que contienen. Si tuviéramos un único dataset y
quisiéramos mostrar los nombres de las clases de entidad, haríamos
Trata de averiguar cómo anidar este bucle for dentro del bucle for implementado en la primera parte del
ejercicio.

'''

fileGDB = [ ['Abastecimiento', ['Estacion de bombeo', 'Tuberia', 'Valvula']], ['Saneamiento', ['Pozos', 'Colectores']]]

for dataset in fileGDB:
    print("Dataset: {}".format(dataset[0]))
    print("Capas : ")
    for capa in dataset[1]:
        print(" {}".format(capa))

print("--------")