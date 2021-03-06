import folium
import pandas
# Volcanoes across the  world Data Set.
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
# making a color profile according to the elevation in the volcanoes data set. .
# def color_producer(elevation):
    if elevation<1000:
        return'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return'red'
    
  # creating the base map   
map = folium.Map(location = [38.58,-99.09],zoom_start=6,tiles="Mapbox Bright")
# Adding  Circle markers
fg = folium.FeatureGroup(name="My Map")
fgp = folium.FeatureGroup(name="Population")

for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location = [lt,ln,el],radius=6, popup=str(el)+"m",fill_color=color_producer(el),color='grey',fill_opacity=0.7))
# Adding a polygon layer to the whole world map.
 fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read()))
map.add_child(fgp)
map.add_child(fg)
# Adding a control layer in the map
map.add_child(folium.LayerControl())
map.save("Map3.html")
