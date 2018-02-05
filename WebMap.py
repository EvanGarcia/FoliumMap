import folium
import pandas

#Receive data about Volcanoes in the USA
data = pandas.read_csv("Volcanoes_USA.txt")

#Create lists of latitude, longitude, and elevation data
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#Set colors for certain elevation levels
def elevationcolor(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

#Initialize map at these coordinates
map = folium.Map(location = [33.4274,-117.612], zoom_start = 10, tiles = "Mapbox Bright")

#Add volcano feature to map
fgv = folium.FeatureGroup(name = "Volcanoes")

#Add volcano markers to map
for lt, ln, el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 6,  popup = str(el) + " m", fill_color =elevationcolor(el), fill = 'true',
    color = 'grey', fill_opacity = 0.7))

# Add population feature to map
fgp = folium.FeatureGroup(name = "Population")

#Add borders, and color filling to map depending on country population
fgp.add_child(folium.GeoJson(data= open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function= lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


#Add layers to map
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

#Save map as html file
map.save("Map.html")
