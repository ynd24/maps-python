from cmath import nan
from turtle import width
import folium
from numpy import NaN
import pandas
import re


def color_of_height(height):
    if (height < 1500):
        return 'blue'
    elif (height < 2500):
        return 'orange'
    else:
        return 'red'

data = pandas.read_csv("Webmap_datasources/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
type = list(data["TYPE"])
loc = list(data["LOCATION"])

html1 = """
Volcano name:
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m <br>
Type: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a> <br>
Location: %s
"""

data2 = pandas.read_csv("Webmap_datasources/volc.csv", sep=";")
 
coord = list(data2["Coordinates"])
lat2 = [] 
lon2 = [] 
Coord = []

def coord_to_lat_lon(list1, list2):
    for c in coord:
        x = re.split(",", c)
        Coord.append(x)
    for lat_long in Coord:
        list1.append(float(lat_long[0]))
        list2.append(float(lat_long[1]))

coord_to_lat_lon(lat2, lon2)

elev2 = list(data2["Elevation"])
country = list(data2["Country"])
type2 = list(data2["Volcano Type"])
year = list(data2["Year"])
name2 = list(data2["Volcano Name"])
deaths = list(data2["Volcano : Deaths"])

html2 = """
Volcano name:
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m <br>
Type: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a> <br>
Eruption Year: %s <br>
Location: %s <br>
Deaths: %s <br>
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name = "volcs in the USA")

for lt, ln, el, name, ty, lc in zip(lat, lon, elev, name, type, loc):
    iframe = folium.IFrame(html=html1 % (name, name, el, ty, ty, lc), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), 
    icon = folium.Icon(color = color_of_height(el))))

fg2 = folium.FeatureGroup("Erupted Volcanoes")

for el, cntry, ty, yr, nm, lt, ln, dhts in zip(elev2, country, type2, year, name2, lat2, lon2, deaths):
    iframe2 = folium.IFrame(html = html2 %(nm, nm, el, ty, ty, yr, cntry, dhts), width = 200, height = 120)
    fg2.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe2), 
    icon = folium.Icon(color = color_of_height(el), icon = "fire", prefix = "fa" )))



map.add_child(fg)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save("Map_html_popup_advanced.html")