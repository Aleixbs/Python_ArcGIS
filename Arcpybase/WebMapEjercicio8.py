'''
Vamos a suponer un WebMap como un conjunto de capas dentro de las cuales podemos distinguir si cada
capa se trata de un mapabase o se trata de una capa operacional.
Dada entonces la siguiente definición abstracta para un WebMap:
webmap = [ [“Topografico”, “basemap”], [“Alumbrado”, “operational”], [“Alcantarillado”,
“operational”] ]

• Haz un programa que indique al usuario el número total de capas operacionales. Puede utilizar
la función “len” ya vista con anterioridad.
• Haz un programa que muestre al usuario los nombres de las capas operacionales.
• Haz un programa que busque el mapabase y cambie su valor para que quede registrado el valor
“Callejero”.
'''

webmap = [ ['Topografico', 'basemap'], ['Alumbrado', 'operational'], ['Alcantarillado',
'operational'] ]

print("Las capas totales en el WebMap son: {}".format(len(webmap)))

capasOperacionales = []
for capa in webmap:
    if capa[1] == "operational":
        capasOperacionales.append(capa[0])
        print("{} es una capa operacional".format(capa[0]))
print("Las capas operacionales són: {}".format(capasOperacionales))

for capa in webmap:
    if capa[1] == "basemap":
        capa[0] = "Callejero"
print(webmap)

