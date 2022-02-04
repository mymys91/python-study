import folium

map = folium.Map(location=[50.09097622909903, 14.315200083211538], zoom_start=7, tiles="Stamen Terrain")
map.add_child(folium.Marker(location=[50.1, 14.4], popup="Hi I am a Marker", icon=folium.Icon(color='blue')))

fg = folium.FeatureGroup(name="My Map")
for coordinate in [[50.3,14.6], [52.3,15.6],[53.3,12.6],[56.1,14.9]]:
    fg.add_child(folium.Marker(location=coordinate, popup="Hi I am the coordinate", icon=folium.Icon(color='orange')))

map.add_child(fg)
map.save("Map1.html")