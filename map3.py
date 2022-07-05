import folium
import pandas
import json
 

 
data1 = json.load(open('Webmap_datasources/world.json', encoding='utf-8-sig'))
 

 
map = folium.Map(location=[41.089742,-118.420348], tile="Stamen", zoom_start=2)
 
fgp = folium.FeatureGroup(name = "Wrold Population")    
fgp.add_child(folium.features.GeoJson(data=data1,  
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 20000000 else 'yellow' 
        if 20000000 <= x['properties']['POP2005'] < 50000000 else 'orange' if 50000000 <= x['properties']['POP2005'] < 100000000
            else 'red'}, tooltip = folium.features.GeoJsonTooltip(fields=['NAME','AREA','POP2005', 'LON', 'LAT'],
                aliases=['NAME:','AREA:','POPULATION:', 'LONGITUDE:', 'LATITUDE:'],
                    style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"))))
 
 
 

map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map3pop.html")
 