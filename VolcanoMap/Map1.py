#!/usr/bin/env python3
# from VolcanoFunc import color_producer - removed because no longer needed
import folium
import pandas

data = pandas.read_csv('MapData/Volcanoes.txt')
# lat = list(data['LAT'])
# lon = list(data['LON'])
# elev = list(data['ELEV'])
# The above is commented out bc variables are not needed

volcano_map = folium.Map(location=[38.5, -99.09], zoom_start=5, tiles='Stamen Terrain')
# created map

fgp = folium.FeatureGroup(name='Population')
fgv = folium.FeatureGroup(name='Volcanoes')
# Made feature groups which can be added to the map in the future


for lt, ln, el in zip(list(data['LAT']), list(data['LON']), list(data['ELEV'])):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=str(el)+"m",))
# adds markers where there are volcanoes in the States


fgp.add_child(folium.GeoJson(data=open('MapData/world.json', 'r', encoding ='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
# makes countries color coded based on population
 

volcano_map.add_child(fgv)
volcano_map.add_child(fgp)
volcano_map.add_child(folium.LayerControl())
volcano_map.save('Map1.html')
# finally add feature groups to map and add layer control